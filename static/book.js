document.addEventListener('DOMContentLoaded', function () {
    const viewIcons = document.querySelectorAll('.view-icon');
    const booksGrid = document.querySelector('.books-grid');

    if (viewIcons && booksGrid) {
        viewIcons.forEach(icon => {
            icon.addEventListener('click', function () {
                viewIcons.forEach(i => i.classList.remove('active'));
                this.classList.add('active');
                const cols = parseInt(this.getAttribute('data-cols'), 10) || 3;
                booksGrid.style.gridTemplateColumns = `repeat(${cols}, minmax(180px, 1fr))`;
            });
        });
    }

    // Placeholder actions for Add to Cart buttons
    document.querySelectorAll('.add-to-cart').forEach(btn => {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            const card = this.closest('.book-card');
            const title = card ? (card.querySelector('h3')?.textContent || 'Book') : 'Book';
            alert(`${title} added to cart (placeholder)`);
        });
    });

    // SORT dropdown (FEATURED)
    const sortDropdown = document.querySelector('.sort-dropdown');
    if (sortDropdown) {
        const sortBtn = sortDropdown.querySelector('.sort-btn');
        const sortMenu = sortDropdown.querySelector('.dropdown-menu');

        const openSort = () => {
            sortDropdown.classList.add('open');
            sortBtn.setAttribute('aria-expanded', 'true');
            sortMenu.setAttribute('aria-hidden', 'false');
        };

        const closeSort = () => {
            sortDropdown.classList.remove('open');
            sortBtn.setAttribute('aria-expanded', 'false');
            sortMenu.setAttribute('aria-hidden', 'true');
        };

        sortBtn.addEventListener('click', function (e) {
            e.stopPropagation();
            if (sortDropdown.classList.contains('open')) closeSort(); else openSort();
        });

        sortMenu.querySelectorAll('li').forEach(li => {
            li.addEventListener('click', function (e) {
                e.stopPropagation();
                const sortKey = this.getAttribute('data-sort');
                const label = this.textContent.trim();
                sortBtn.childNodes[0].nodeValue = label + ' ';
                closeSort();
                console.log('Sort selected:', sortKey);
            });
        });

        document.addEventListener('click', function (e) {
            if (!sortDropdown.contains(e.target)) closeSort();
        });

        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') closeSort();
        });
    }

    // CATEGORY dropdown (BOOKS)
    const categoryDropdown = document.querySelector('.category-dropdown');
    if (categoryDropdown) {
        const catBtn = categoryDropdown.querySelector('.category-btn');
        const catMenu = categoryDropdown.querySelector('.category-menu');

        const openCat = () => {
            categoryDropdown.classList.add('open');
            catBtn.setAttribute('aria-expanded', 'true');
            catMenu.setAttribute('aria-hidden', 'false');
        };

        const closeCat = () => {
            categoryDropdown.classList.remove('open');
            catBtn.setAttribute('aria-expanded', 'false');
            catMenu.setAttribute('aria-hidden', 'true');
        };

        catBtn.addEventListener('click', function (e) {
            e.stopPropagation();
            if (categoryDropdown.classList.contains('open')) closeCat(); else openCat();
        });

        catMenu.querySelectorAll('li').forEach(li => {
            li.addEventListener('click', function (e) {
                e.stopPropagation();
                const cat = this.getAttribute('data-cat');
                const label = this.textContent.trim();
                catBtn.childNodes[0].nodeValue = label + ' ';
                closeCat();
                console.log('Category selected:', cat);
            });
        });

        document.addEventListener('click', function (e) {
            if (!categoryDropdown.contains(e.target)) closeCat();
        });

        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') closeCat();
        });
    }

});
