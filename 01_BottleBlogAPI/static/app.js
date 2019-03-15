const app = new window.Vue({
  template: "#appTemplate",
  data: () => ({ title: "Title", author: "Author", htmlBody: "<b>Test</b>" }),
  created() {
    const md = window.markdownit();
    // Use the URL as the path for the API request (dirty router solution)
    fetch("/api" + window.location.pathname)
      .then(response => response.json())
      .then(data => {
        this.title = data.title;
        this.author = data.author;
        this.htmlBody = md.render(data.body); // TODO: Parse markdown
      });
  }
});
app.$mount("#app");
