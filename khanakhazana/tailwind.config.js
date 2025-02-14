/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [

    //root_directory/templates/subdirectory/home.html
    './templates/**/*.html',

    //root_directory/app_name/templates/app_name/home.html
    './*/templates/**/*.html',

    
    



  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

