<template>
  <div class="infoPop">
    <div class="tabPop">
      <div class="tab1 tab">
        <button class="extraTab tabtext text" @click="swapMain">
          {{ name }}
        </button>
        <button class="exitbtn heading" @click="exit">X</button>
      </div>
      <div class="tab tab2" v-if="this.store.vendorHeader">
        <button class="vendorTab tabtext text" @click="swapVendor">
          {{ vendor }}
        </button>
        <button class="exitbtn heading" @click="closeVendor">X</button>
      </div>
      <div class="tab tab3" v-if="this.store.categoryHeader">
        <button class="vendorTab tabtext text" @click="swapCat">
          {{ category }}
        </button>
        <button class="exitbtn heading" @click="closeCat">X</button>
      </div>
    </div>
    <div
      class="extraInfoPanel"
      v-if="this.store.vendor === false && this.store.categoryPop === false"
    >
      <Extra
        :img_link="img_link"
        :name="name"
        :category="category"
        :quantity="quantity"
        :link="link"
        :vendor="vendor"
        :date="date"
      />
    </div>
    <div class="extraInfoPanel" v-if="this.store.vendor">
      <VendorInfo />
    </div>
    <div class="extraInfoPanel" v-if="this.store.categoryPop">
      <CategoryInfo />
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
.tabPop {
  min-height: 5.5rem;
  border-bottom: var(--border);
  display: flex;
  flex-direction: row;
}

.tab {
  height: 100%;
  margin-top: 0;
  display: flex;
  justify-content: space-between;
  border-right: var(--border);
  align-items: center;
  min-width: 30%;
}
.tabtext {
  border: none;

  background-color: var(--whitebg);
  padding-left: 1rem;
  padding-right: 1rem;

  height: 100%;
}
.extraTab {
  max-width: 80%;
  width: fit-content;
  overflow: hidden;

  white-space: nowrap;
  text-overflow: ellipsis;
}
.tab1 {
  max-width: 100%;
}
.tab2,
.tab3 {
  max-width: 100%;
}

.vendorTab {
  width: fit-content;
}
.exitbtn {
  margin-right: 2rem;
  color: var(--darkergray);
  transition: all 0.1s;
}
.exitbtn:hover {
  cursor: pointer;
  color: var(--darkestgray);
}
.extraInfoPanel {
  height: 100%;
  width: 100%;
}
</style>

<script>
import { useItemsStore } from "~/store/ItemsStore";
import Extra from "./extra.vue";
import VendorInfo from "./vendorInfo.vue";
import CategoryInfo from "./categoryInfo.vue";

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
  components: {
    Extra,
    VendorInfo,
    CategoryInfo,
  },
  data() {
    return {
      store: useItemsStore(),
    };
  },
  methods: {
    closeVendor() {
      this.store.$patch({ vendor: false, vendorHeader: false });
      console.log(this.store.vendor);
    },
    closeCat() {
      this.store.$patch({ categoryPop: false, categoryHeader: false });
    },
    exit() {
      this.store.$patch({ info: false });
      this.closeVendor();
      this.closeCat;
      this.store.resizing();
    },
    swapMain() {
      this.store.$patch({ vendor: false, categoryPop: false });
    },
    swapVendor() {
      this.store.$patch({ vendor: true, categoryPop: false });
    },
    swapCat() {
      this.store.$patch({ vendor: false, categoryPop: true });
    },
  },
};
</script>
