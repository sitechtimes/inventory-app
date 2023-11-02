<template>
  <div class="container">
    <div class="category-cont">
      <div class="category" v-for="items in category" :key="items">
        <div>{{ items.category_name }}</div>
        <div>
          <button
            class="item-btn"
            v-for="supply in items.itemsCategory"
            :key="supply"
            @click="$emit('item', supply.id)"
          >
            <div class="item-cont">
              <div class="image-cont">
                <img class="image" :src="supply.image" alt="item-image" />
              </div>
              <div class="item-text">
                <div class="supply-name-cont">
                  <h5 class="supply-name">{{ supply.name }}</h5>
                </div>
                <div class="total-cont">
                  <h5>Total: {{ supply.total }}</h5>
                </div>
              </div>
            </div>
          </button>
        </div>
      </div>
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
      console.log(data);
      category.value = data;
    });
});
</script>

<style scoped>
.container {
  display: flex;
  flex-flow: row nowrap;
  width: 98vw;
}
.category-cont {
  display: flex;
  flex-flow: column nowrap;
  width: 70vw;
}
.cont {
  width: 25rem;
  background-color: gray;
}
.item-btn {
  width: 20rem;
  height: 8rem;
}
.item-cont {
  width: 100%;
  height: 100%;
  background-color: rgb(223, 220, 220);
  opacity: 0.8;
  border: none;
  display: flex;
  flex-flow: row nowrap;
}
.image-cont {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 5rem;
  height: 8rem;
}
.image {
  width: 5rem;
  height: 5rem;
}
.item-text {
  width: 15rem;
  height: 8rem;
  display: flex;
  flex-flow: column nowrap;
}
.supply-name-cont {
  width: 15rem;
  height: 5rem;
}
.supply-name {
  font-size: 0.9rem;
  font-weight: 300;
}
.total-cont {
  width: 15rem;
  height: 3rem;
}
</style>
