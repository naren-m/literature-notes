module.exports = {
    pathPrefix: "/literature-notes",  // Replace with your repository name
    plugins: [
      {
        resolve: "gatsby-theme-garden",
        options: {
          rootNote: "/literature-notes",
          contentPath: "/literature-notes/notes",
        },
      },
    ],
  };