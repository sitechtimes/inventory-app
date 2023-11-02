<template>
  <div>
    <div class="cont">
      <button v-for="tags in category" :key="tags">
        <h5>{{ tags.category_name }}</h5>
        <h5>({{ tags.count }})</h5>
      </button>
    </div>
  </div>
</template>

<script setup>
let category = ref([]);
const config = useRuntimeConfig()

onMounted(() => {
  fetch(`${config.public.protocol}://${config.public.baseurl}:${config.public.port}/items/category/`, {
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
      category.value = data;
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
