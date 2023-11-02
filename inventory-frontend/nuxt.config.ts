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
      baseurl: 'localhost',
      port: '8000',
      protocol: "http"
    }
  }
});
