<template>
  <div
    class="itemMonitor"
    :class="blue(name) ? 'activeBlue' : ''"
    ref="main"
    @mousedown="clickedMonitor"
  >
    <div class="nameM text" ref="name">{{ name }}</div>
    <div class="quantityM smalltext" ref="quant">{{ quantity }}</div>
  </div>
</template>

<script>
import { useItemsStore } from "~/store/ItemsStore";

export default {
  name: "ItemMonitor",
  props: {
    name: String,
    quantity: Number,
    image: String,
    vendor: String,
    link: String,
    updated: String,
    category: String,
    makerspace: Number,
    backroom: Number,
  },
  data() {
    return {
      store: useItemsStore(),
    };
  },
  methods: {
    blue(insert) {
      if (this.store.popup.name === insert && this.store.info === true) {
        return true;
      } else {
        return false;
      }
    },
    clickedMonitor() {
      if (this.store.popup.name === this.name) {
        if (this.store.info === false) {
          this.store.$patch({ info: true });
        } else {
          this.store.$patch({
            info: false,
            vendor: false,
            vendorHeader: false,
            categoryPop: false,
            categoryHeader: false,
          });
        }
      } else {
        this.store.$patch({
          popup: {
            image: this.image,
            name: this.name,
            category: this.category,
            quantity: this.quantity,
            link: this.description,
            vendor: this.vendor,
            date: this.updated,
            makerspace: this.makerspace,
            backroom: this.backroom,
          },
        });
        this.store.$patch({
          info: true,
          vendor: false,
          vendorHeader: false,
          categoryPop: false,
          categoryHeader: false,
        });
      }
      if (this.store.dismiss === false) {
        this.store.NavMenu();
      }
      const bigdivM = document.querySelector(".bigdivM");
      if (this.store.info === true) {
        bigdivM.style.flexDirection = "row";
      } else {
        bigdivM.style.flexDirection = "column";
      }
    },
  },
};
</script>

<style>
.nameM {
  padding: 1rem;
  padding-left: 2.5rem;
  overflow: hidden;

  white-space: nowrap;
  text-overflow: ellipsis;
  width: 60%;
  max-width: 70rem;
}

.quantityM {
  height: 100%;

  padding: 1rem 2rem;
}
.itemMonitor {
  background-color: var(--whitebg);
  border-bottom: var(--border);
  display: flex;
  align-items: center;
  width: 100%;
  transition: all 0.2s;
}
.itemMonitor:hover {
  background-color: var(--lightblue);
}
.activeBlue {
  background-color: var(--lightblue);
}
</style>
