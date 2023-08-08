<template>
  <div class="popUpPanel">
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
        <button class="text col2 extrabtn" @click="categoryInfo">
          {{ category }}
        </button>
      </div>
      <div class="detailsStock poprow">
        <div class="text col1">Total Stock Available</div>
        <div class="text col2">
          {{ quantity }}
        </div>
      </div>
      <div class="detailsPurchase poprow">
        <div class="text col1">Purchase Link</div>
        <a class="text col2" :href="link">{{ link }}</a>
      </div>
      <div class="detailsVendor poprow">
        <div class="text col1">Vendor</div>
        <button class="text extrabtn col2" @click="vendorInfo">
          {{ vendor }}
        </button>
      </div>
      <div class="detailsDate poprow">
        <div class="text col1">Date Last Purchased</div>
        <div class="text col2">{{ date }}</div>
      </div>
    </div>
    <div class="logPop">
      <div class="subheading changelog">Inventory Change Log</div>
      <button class="text logorg">DateTime</button>
    </div>
  </div>
</template>

<script>
import { useItemsStore } from "~/store/ItemsStore";
export default {
  name: "Extra",
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
    vendorInfo() {
      this.store.$patch({ vendor: true, vendorHeader: true });
      this.store.inactive(".extraTab", ".tab1", ".tab1btn");
      if (this.store.categoryHeader) {
        this.store.inactive(".categoryTab", ".tab3", ".tab3btn");
      }
      this.store.active(".vendorTab", ".tab2", ".tab2btn");
    },
    categoryInfo() {
      this.store.$patch({ categoryPop: true, categoryHeader: true });
      if (this.store.vendorHeader) {
        this.store.inactive(".vendorTab", ".tab2", ".tab2btn");
      }
      this.store.inactive(".extraTab", ".tab1", ".tab1btn");
      this.store.active(".categoryTab", ".tab3", ".tab3btn");
    },
  },
};
</script>

<style>
.popUpPanel {
  height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
}

.imagePop {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 20%;
  margin-top: 2rem;
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
  padding-right: 5rem;
}
.extrabtn {
  width: 20%;
  text-align: left;
}
.extrabtn:active {
  box-shadow: 0.2rem 0.2rem 1rem var(--tpdarkgray);
}
.changelog,
.logorg {
  padding: 1.5rem;
  border-bottom: var(--border);
}
.changelog {
  border-top: var(--border);
}

.logorg {
  text-align: left;
  width: 100%;
  font-weight: 400;
}
</style>
