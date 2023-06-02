$(document).ready(function () {
  var tabButtons = $(".tab-button");
  var tabs = $(".tab");

  var activeTab = tabs.first();
  activeTab.addClass("active");
  activeTab.show();

  tabButtons.click(function () {
    var index = $(this).index();

    tabs.removeClass("active");
    tabs.hide();

    tabs.eq(index).addClass("active");
    tabs.eq(index).show();
  });
});
