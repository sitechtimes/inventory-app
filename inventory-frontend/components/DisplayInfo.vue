<template>
  <div>
    <ItemButtons @item="displayItem" />
    <div class="cont">
      <div v-if="item.id" class="item-cont">
        <div class="main">
          <h4 class="itemName">{{ item.name }}</h4>
          <img :src="item.image" class="itemImage" />
          <div class="alert" v-if="item.alert">
            <font-awesome-icon
              :icon="['fas', 'triangle-exclamation']"
              class="alert-icon"
            />
            <h3 class="alert-text">Low on this Supply</h3>
          </div>
          <h4 class="itemLocation">Location: {{ item.location }}</h4>
        </div>

        <div class="moveItems">
          <MoveItems :id="item.id" />
        </div>

        <div class="Purchase">
          <h4 class="itemVendor">Vendor: {{ item.vendor }}</h4>
          <h4 class="itemLink">
            Purchase Link:
            <a :href="item.purchase_link">{{ item.purchase_link }}</a>
          </h4>
          <h4 class="LastPurchased">
            Last Purchase: {{ item.last_purchased }}
          </h4>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
let item = ref({});
function displayItem(itemId) {
  const config = useRuntimeConfig()
  fetch(`${config.protocol}://${config.baseurl}:${config.port}/CurrentItem/${itemId}/`, {
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
      item.value = data;
    });
}



</script>

<style scoped>
.cont {
  width: 21rem;
  height: 50rem;
  background-color: rgb(209, 204, 204);
}
.item-cont {
  display: flex;
  flex-flow: column nowrap;
  align-items: center;
  width: 100%;
  height: 100%;
}
.item-name {
  height: 5rem;
}
.main {
  width: 20rem;
  height: 28rem;
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  align-items: center;
}
.itemImage {
  width: 18rem;
  height: 18rem;
}
.moveItems {
  width: 20rem;
  height: 10rem;
}
.Purchase {
  position: relative;
  width: 20rem;
  height: 5rem;
}
.itemLink {
  height: 3.5rem;
  overflow: hidden;
}
.alert {
  position: relative;
  width: 20rem;
  height: 4rem;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-flow: column nowrap;
}
.alert-icon {
  width: 3rem;
  height: 3rem;
  color: red;
}
.alert-text {
  color: red;
}
</style>
