module.exports = {
    pathPrefix: "/literature-notes",  // Replace with your repository name
    plugins: [
      {
        resolve: "gatsby-theme-garden",
        options: {
          rootNote: "/path/to/your/root-note",
          contentPath: "/path/to/your/foam-notes",
        },
      },
    ],
  };