<template>
  <div class="infoPop">
    <button class="exitbtn heading" @click="exit">X</button>
    <div class="imagePop">
      <img class="imagePopView" :src="img_link" />
    </div>
    <div class="detailsPop">
      <div class="detailsName poprow">
        <div class="text col1">Name</div>
        <div class="text col2">{{ name }}</div>
      </div>

      <div class="detailsCat poprow">
        <div class="text col1">Category</div>
        <div class="text col2">{{ category }}</div>
      </div>
      <div class="detailsStock poprow">
        <div class="text col1">Total Stock Available</div>
        <div class="text col2">{{ quantity }}</div>
      </div>
      <div class="detailsPurchase poprow">
        <div class="text col1">Purchase Link</div>
        <a class="text col2" :href="link">{{ link }}</a>
      </div>
      <div class="detailsVendor poprow">
        <div class="text col1">Vendor</div>
        <div class="text col2">{{ vendor }}</div>
      </div>
      <div class="detailsDate poprow">
        <div class="text col1">Date Last Purchased</div>
        <div class="text col2">{{ date }}</div>
      </div>
    </div>
    <div class="logPop">
      <div class="text">Inventory Change Log</div>
    </div>
  </div>
</template>

<style>
.infoPop {
  height: 100%;
  width: 100%;

  background-color: var(--whitebg);
  display: flex;
  flex-direction: column;
}
.imagePop {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 20%;
}
.imagePopView {
  max-height: 80%;
  max-width: 80%;
  object-fit: scale-down;
}
.poprow {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  margin: 2rem;
  height: fit-content;
  width: 100%;
}
.col1 {
  margin-left: 2rem;
  margin-right: 2rem;
  min-width: 10rem;
  width: 20%;
  color: var(--darkestgray);
}
.col2 {
  width: 70%;
  padding-right: 2rem;
}
.exitbtn {
  background-color: var(--whitebg);
  border: none;
  position: absolute;
  top: 3rem;
  right: 3rem;
  color: var(--darkergray);
  transition: all 0.1s;
}
.exitbtn:hover {
  cursor: pointer;
  color: var(--darkestgray);
}
</style>

<script>
import { useItemsStore } from "~/store/ItemsStore";

export default {
  name: "Info",
  props: {
    img_link: String,
    name: String,
    category: String,
    quantity: Number,
    link: String,
    vendor: String,
    date: String,
  },
  data() {
    return {
      store: useItemsStore(),
    };
  },
  methods: {
    exit() {
      this.store.$patch({ info: false });
    },
  },
};
</script>
