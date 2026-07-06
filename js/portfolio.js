$(document).ready(function() {
    // Check if portfolio exists
    if ($('.portfolio-grid').length === 0) return;

    // Initialize original order for sorting
    $('.portfolio-card').each(function(index) {
        $(this).attr('data-index', index);
    });

    // Filter functionality
    $('.filter-btn').on('click', function(e) {
        e.preventDefault();
        $('.filter-btn').removeClass('active');
        $(this).addClass('active');
        filterCards();
    });

    // Search functionality
    $('.portfolio-search button').on('click', function(e) {
        e.preventDefault();
        filterCards();
    });
    
    $('.portfolio-search input').on('keyup', function() {
        filterCards();
    });

    // Sorting functionality
    $('.portfolio-actions select').on('change', function() {
        sortCards();
    });

    // View toggle functionality
    $('.view-btn').on('click', function(e) {
        e.preventDefault();
        $('.view-btn').removeClass('active');
        $(this).addClass('active');
        
        var isList = $(this).find('.fa-bars').length > 0;
        
        if (isList) {
            $('.portfolio-grid').css({'grid-template-columns': '1fr'});
            $('.portfolio-card').css({'display': 'flex', 'align-items': 'center'});
            $('.card-img').css({'width': '300px', 'height': '200px', 'flex-shrink': '0'});
            $('.card-body').css({'flex': '1'});
        } else {
            $('.portfolio-grid').css({'grid-template-columns': ''});
            $('.portfolio-card').css({'display': '', 'align-items': ''});
            $('.card-img').css({'width': '', 'height': '', 'flex-shrink': ''});
            $('.card-body').css({'flex': ''});
        }
    });

    function filterCards() {
        var activeFilter = $('.filter-btn.active').text().trim();
        var searchQuery = $('.portfolio-search input').val().trim().toLowerCase();
        var visibleCount = 0;
        
        $('.portfolio-card').each(function() {
            var $card = $(this);
            var category = $card.find('.card-badge').text().trim();
            var title = $card.find('.card-title').text().trim().toLowerCase();
            var meta = $card.find('.card-meta').text().trim().toLowerCase();
            
            var matchFilter = (activeFilter === '전체' || category === activeFilter);
            var matchSearch = (searchQuery === '' || title.indexOf(searchQuery) !== -1 || meta.indexOf(searchQuery) !== -1);
            
            if (matchFilter && matchSearch) {
                // Use css display block explicitly, but wait, grid items shouldn't be flex or block, just empty resets to grid/flex context
                // Let's remove any inline display:none
                $card.css('display', '');
                visibleCount++;
            } else {
                // Force hide
                $card.css('display', 'none');
            }
        });
        
        // Update total count
        $('.portfolio-total strong').text(visibleCount);
        
        // Re-apply list view styles to visible elements if list view is active
        if ($('.view-btn .fa-bars').parent().hasClass('active')) {
            $('.portfolio-card').not('[style*="display: none"]').css({'display': 'flex'});
        }
    }

    function sortCards() {
        var sortType = $('.portfolio-actions select').val();
        var $grid = $('.portfolio-grid');
        var $cards = $grid.children('.portfolio-card').get();
        
        $cards.sort(function(a, b) {
            var titleA = $(a).find('.card-title').text().trim();
            var titleB = $(b).find('.card-title').text().trim();
            
            if (sortType === '이름순') {
                return titleA.localeCompare(titleB, 'ko');
            } else {
                // 최신순 (Original index)
                var idxA = parseInt($(a).attr('data-index')) || 0;
                var idxB = parseInt($(b).attr('data-index')) || 0;
                return idxA - idxB;
            }
        });
        
        $.each($cards, function(index, item) {
            $grid.append(item); // Re-append reorders them
        });
    }
});
