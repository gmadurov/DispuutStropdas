// this section combines the pagination and the searchquery into on working thing
// get serarcg form and page
let searchForm = document.getElementById("searchForm");
let pageLinks = document.getElementsByClassName("page-link");

// ensure search form exists
if (searchForm) {
  for (let i = 0; pageLinks.length > i; i++) {
    pageLinks[i].addEventListener("click", function (e) {
      e.preventDefault();
      // get the data page
      let page = this.dataset.page;
      //
      searchForm.innerHTML += `<input value=${page} name='page' hidden/>`;
      searchForm.submit();
    });
  }
}
