from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta, date
import json

from .models import Author, Genre, Book, BookInstance, Borrowing


@login_required
def dashboard(request):
    today = date.today()

    # ── Top-level stats ────────────────────────────────────────────────────
    total_books = Book.objects.count()
    total_copies = BookInstance.objects.count()
    available_copies = BookInstance.objects.filter(is_available=True).count()
    total_authors = Author.objects.count()
    total_genres = Genre.objects.count()
    total_members = User.objects.filter(is_staff=False).count()
    active_borrowings = Borrowing.objects.filter(is_returned=False).count()
    overdue_borrowings = Borrowing.objects.filter(
        is_returned=False,
        due_date__lt=today
    ).count()

    # ── Borrowing trend — last 6 months ───────────────────────────────────
    months_labels = []
    borrowed_counts = []
    returned_counts = []
    for i in range(5, -1, -1):
        month_start = (today.replace(day=1) - timedelta(days=i * 30))
        month_start = month_start.replace(day=1)
        if month_start.month == 12:
            month_end = month_start.replace(year=month_start.year + 1, month=1, day=1)
        else:
            month_end = month_start.replace(month=month_start.month + 1, day=1)

        borrowed = Borrowing.objects.filter(
            borrow_date__date__gte=month_start,
            borrow_date__date__lt=month_end
        ).count()
        returned = Borrowing.objects.filter(
            return_date__date__gte=month_start,
            return_date__date__lt=month_end
        ).count()

        months_labels.append(month_start.strftime("%b"))
        borrowed_counts.append(borrowed)
        returned_counts.append(returned)

    # ── Genre distribution ─────────────────────────────────────────────────
    genre_qs = Genre.objects.annotate(book_count=Count('books')).order_by('-book_count')[:8]
    genre_labels = [g.name for g in genre_qs]
    genre_counts = [g.book_count for g in genre_qs]

    # ── Copy condition breakdown ───────────────────────────────────────────
    condition_qs = (
        BookInstance.objects
        .values('condition')
        .annotate(count=Count('id'))
        .order_by('condition')
    )
    condition_map = {c['condition']: c['count'] for c in condition_qs}
    condition_labels = ['Excellent', 'Good', 'Fair', 'Damaged']
    condition_counts = [condition_map.get(k.lower(), 0) for k in condition_labels]

    # ── Recent borrowings ──────────────────────────────────────────────────
    recent_borrowings = (
        Borrowing.objects
        .select_related('borrower', 'book_instance', 'book_instance__book')
        .order_by('-borrow_date')[:10]
    )
    borrowings_data = []
    for b in recent_borrowings:
        if b.is_returned:
            status = 'returned'
        elif b.due_date < today:
            status = 'overdue'
        else:
            status = 'active'
        borrowings_data.append({
            'id': b.id,
            'user': b.borrower.username,
            'book': b.book_instance.book.title,
            'borrow_date': b.borrow_date.strftime('%Y-%m-%d'),
            'due_date': b.due_date.strftime('%Y-%m-%d'),
            'status': status,
        })

    avail_pct = round((available_copies / total_copies * 100) if total_copies else 0)

    context = {
        'total_books': total_books,
        'total_copies': total_copies,
        'available_copies': available_copies,
        'avail_pct': avail_pct,
        'total_authors': total_authors,
        'total_genres': total_genres,
        'total_members': total_members,
        'active_borrowings': active_borrowings,
        'overdue_borrowings': overdue_borrowings,
        'months_labels': json.dumps(months_labels),
        'borrowed_counts': json.dumps(borrowed_counts),
        'returned_counts': json.dumps(returned_counts),
        'genre_labels': json.dumps(genre_labels),
        'genre_counts': json.dumps(genre_counts),
        'condition_labels': json.dumps(condition_labels),
        'condition_counts': json.dumps(condition_counts),
        'borrowings_data': borrowings_data,
    }
    return render(request, 'book/dashboard.html', context)