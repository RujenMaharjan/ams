window.onscroll = function () {
    handleNavbar();
  };
  
  const navbar = document.getElementById("navbar");
  const sticky = 100; // Adjust this value to control when the navbar becomes visible
  
  function handleNavbar() {
    if (window.pageYOffset > sticky) {
      navbar.classList.add("visible");
    } else {
      navbar.classList.remove("visible");
    }
  }
  
  // Add event listener to the like buttons to prevent propagation and trigger custom event
  document.querySelectorAll(".like-btn").forEach((button) => {
    button.addEventListener("click", function (event) {
      event.stopPropagation(); // Prevent click event from propagating to the card link
      event.preventDefault(); // Prevent form submission
  
      // Custom like action (toggle button color)
      if (button.classList.contains("liked")) {
        button.classList.remove("liked");
        console.log("Like removed");
      } else {
        button.classList.add("liked");
        console.log("Liked");
      }
    });
  });
  