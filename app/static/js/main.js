// Add to Wishlist
function addToWishlist(productId) {
    fetch(`/wishlist/add/${productId}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          alert('Added to wishlist!');
        } else {
          alert('Failed to add to wishlist.');
        }
      });
  }
  
  // Add to Cart
  function addToCart(productId) {
    fetch(`/cart/add/${productId}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          alert('Added to cart!');
        } else {
          alert('Failed to add to cart.');
        }
      });
  }
  
  // Load Cart and Wishlist Items
  function loadCartAndWishlist() {
    fetch('/cart/items')
      .then(response => response.json())
      .then(data => {
        const cartItems = document.getElementById('cart-items');
        cartItems.innerHTML = data.items.map(item => `
          <li class="list-group-item">${item.name} - $${item.price}</li>
        `).join('');
      });
  
    fetch('/wishlist/items')
      .then(response => response.json())
      .then(data => {
        const wishlistItems = document.getElementById('wishlist-items');
        wishlistItems.innerHTML = data.items.map(item => `
          <li class="list-group-item">${item.name} - $${item.price}</li>
        `).join('');
      });
  }
  
  // Load cart and wishlist when the sidebar is opened
  document.getElementById('offcanvasCart').addEventListener('show.bs.offcanvas', loadCartAndWishlist);