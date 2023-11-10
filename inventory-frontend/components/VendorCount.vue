<template>
  <div>
    <div class="cont">
      <button v-for="tags in vendor" :key="tags">
        <h5>{{ tags.vendor_name }}</h5>
        <h5>({{ tags.count }})</h5>
      </button>
    </div>
  </div>
</template>

<script setup>
let vendor = ref([]);
onMounted(() => {
  const config = useRuntimeConfig()
  fetch(`${config.public.protocol}://${config.public.baseurl}:${config.public.port}items/vendor/`, {

    method: "GET",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    referrerPolicy: "no-referrer",
  })
    .then((response) => response.json())
    .then((data) => {
      vendor.value = data;
    });
});
</script>

<style scoped>
.cont {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
}
button {
  display: flex;
  flex-flow: row nowrap;
  padding: 0.65rem;
  margin: 1px;
  align-content: center;
}
h5 {
  margin: 1px;
}
</style>
