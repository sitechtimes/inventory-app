// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  ssr: false,
  devtools: { enabled: true },
  css: [
    "@fortawesome/fontawesome-svg-core/styles.css",
    "~/assets/css/main.css",
  ],
  pages: true,
  modules: ["@pinia/nuxt"],

  runtimeConfig: {
    public:{
      baseurl: '100.101.79.68',
      port: '8000',
      protocol: "http"
    }
  }

});
