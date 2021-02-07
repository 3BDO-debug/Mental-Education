function wishlistHandler(condition, courseId) {
  if (condition == "addToWishList") {
    $.ajax({
      type: "GET",
      url: `/View/Wishlist/Course/${courseId}/Wished`,
      success: function () {
        document
          .getElementById("wishlist-successs-notification-toggler")
          .click();
        document.getElementById("wishlist-button").innerHTML =
          "Added to wishlist";
        window.location.reload();
        console.log("course added to wishlist");
      },
      error: function () {
        console.log("course could not be added to wishlist");
      },
    });
  }
}

function courseReviewHandler(courseNameAsSlug) {
  $("#courseReviewForm").submit(function (event) {
    event.preventDefault();
    var form = $(this);
    var url = form.attr("action");
    $.ajax({
      type: "POST",
      url: url,
      async: false,
      data: form.serialize(),
      success: function () {
        document
          .getElementById("review-submit-success-notification-toggler")
          .click();
        
      },
      error: function () {
        console.log("error");
      },
    });
  });
}
