<template>
  <div>
    <button @click="click"></button>
    <div class="content" v-if="show">
      <NuxtLink class="link"> Settings </NuxtLink>
      <NuxtLink class="link"> items </NuxtLink>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
let show = ref(false);

const click = () => {
  if (show.value) {
    show.value = false;
  } else {
    show.value = true;
  }
};
</script>

<style scoped>
button {
  border-radius: 2rem;
  background-color: gray;
  width: 3rem;
  height: 3rem;
  border: none;
}
button:hover {
  cursor: pointer;
}
.content {
  padding: 10px;
  background-color: gray;
  width: 5rem;
  border-radius: 10px;
}
.link {
  margin-top: 10rem;
}
</style>
