// gatsby-config.js
module.exports = {
    plugins: [
      {
        resolve: `gatsby-theme-garden`,
        options: {
          // basePath defaults to `/`
          basePath: `/literature-notes`,
          rootNote: `/literature-notes/notes`,
        //   contentPath: `/notes`,
        },
      },
    ],
  };