<template>
  <div class="infoPop">
    <div class="tabPop">
      <div class="tab1 tab">
        <button class="extraTab tabtext text" @click="swapMain">
          {{ name }}
        </button>
        <button class="exitbtn heading tab1btn" @click="exit">X</button>
      </div>
      <div class="tab tab2" v-if="this.store.vendorHeader">
        <button class="vendorTab tabtext text" @click="swapVendor">
          {{ vendor }}
        </button>
        <button class="exitbtn heading tab2btn" @click="closeVendor">X</button>
      </div>
      <div class="tab tab3" v-if="this.store.categoryHeader">
        <button class="categoryTab tabtext text" @click="swapCat">
          {{ category }}
        </button>
        <button class="exitbtn heading tab3btn" @click="closeCat">X</button>
      </div>
    </div>
    <div class="extraInfoPanel" v-if="this.store.vendor === false && this.store.categoryPop === false">
      <Extra :img_link="img_link" :name="name" :category="category" :quantity="quantity" :link="link" :vendor="vendor"
        :date="date" />
    </div>
    <div class="extraInfoPanel" v-if="this.store.vendor">
      <VendorInfo :vendorName="vendor" />
    </div>
    <div class="extraInfoPanel" v-if="this.store.categoryPop">
      <CategoryInfo :categoryName="category" />
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
  color: var(--darkergray);
  transition: all 0.1s linear;
  border-radius: 3rem;
  height: 5rem;
  width: 5rem;
  background-color: rgba(0, 0, 0, 0);
}

.exitbtn:hover {
  cursor: pointer;
  color: var(--darkestgray);
  background-color: var(--tpgray);
}

.exitbtn:active {
  background-color: var(--tpdarkgray);
}

.extraInfoPanel {
  height: 100%;
  width: 100%;
}

.active {
  background-color: var(--whitebg);
}

.inactive {
  background-color: var(--halflightgray);
  color: var(--darkergray);
  transition: all 0.5s;
}

.inactivebtn {
  opacity: 0;
  background-color: var(--halflightgray);
  transition: all 0.5s;
}

.inactivebtn:hover {
  opacity: 1;
}

.inactive:hover>.inactivebtn {
  opacity: 1;
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
    swapMain() {
      this.store.$patch({ vendor: false, categoryPop: false });
      if (this.store.vendorHeader) {
        this.store.inactive(".vendorTab", ".tab2", ".tab2btn");
      }
      if (this.store.categoryHeader) {
        this.store.inactive(".categoryTab", ".tab3", ".tab3btn");
      }
      this.store.active(".extraTab", ".tab1", ".tab1btn");
    },
    swapVendor() {
      this.store.$patch({ vendor: true, categoryPop: false });
      this.store.inactive(".extraTab", ".tab1", ".tab1btn");
      if (this.store.categoryHeader) {
        this.store.inactive(".categoryTab", ".tab3", ".tab3btn");
      }
      this.store.active(".vendorTab", ".tab2", ".tab2btn");
    },
    swapCat() {
      this.store.$patch({ vendor: false, categoryPop: true });
      if (this.store.vendorHeader) {
        this.store.inactive(".vendorTab", ".tab2", ".tab2btn");
      }
      this.store.inactive(".extraTab", ".tab1", ".tab1btn");
      this.store.active(".categoryTab", ".tab3", ".tab3btn");
    },
    closeVendor() {
      this.store.$patch({ vendor: false, vendorHeader: false });
      console.log(this.store.vendor);
      this.swapMain();
    },
    closeCat() {
      this.store.$patch({ categoryPop: false, categoryHeader: false });
      this.swapMain();
    },
    exit() {
      this.store.$patch({ info: false });
      this.closeVendor();
      this.closeCat();
      this.swapMain();
      if (this.store.catalog) {
        this.store.resizing();
      } else if (this.store.monitor) {
        document.querySelector(".bigdivM").style.flexDirection = "column";
      }
    },
  },
  mounted() { },
};
</script>
