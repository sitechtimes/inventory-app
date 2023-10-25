<template>
  <div class="bigdiv">
    <div id="mainItems">
      <div class="itemHeader subheading">Items</div>

      <div
        class="errorsearch subheading"
        v-if="store.search === true && store.empty === true"
      >
        No Items Found
      </div>
      <div class="itemHolderAll" ref="allItems">
        <div class="categoryHolder" v-if="store.search">
          <ItemPerCat
            v-for="each in store.items"
            :key="each[0]"
            :list="each[1]"
            :name="each[0]"
          ></ItemPerCat>
        </div>
        <div class="categoryHolder" v-else>
          <ItemPerCat
            v-for="each in store.items"
            :key="each.id"
            :list="each.itemsCategory"
            :name="each.category_name"
          ></ItemPerCat>
        </div>
      </div>
    </div>

    <div class="infoDesc" v-if="store.info" ref="infoHolder">
      <Info
        :img_link="store.popup.image"
        :name="store.popup.name"
        :category="store.popup.category"
        :quantity="store.popup.quantity"
        :link="store.popup.link"
        :vendor="store.popup.vendor"
        :date="store.popup.updated"
        :backroom_quantity="store.popup.backroom"
        :makerspace_quantity="store.popup.makerspace"
      />
    </div>
  </div>
</template>

<script>
import ItemPerCat from "./itemPerCat.vue";
import Info from "./info.vue";
import { useItemsStore } from "~/store/ItemsStore";
export default {
  name: "Catalog",
  components: { ItemPerCat, Info },
  data() {
    return {
      store: useItemsStore(),
    };
  },
  methods: {},
  mounted() {},
};
</script>

<style>
.bigdiv {
  display: flex;
  flex-direction: row;

  background-color: var(--lightgray);
  min-width: 100%;
}
#mainItems {
  display: flex;
  flex-direction: column;
  width: 100%;
}
.itemHeader {
  min-height: 5.5rem;
  border-bottom: var(--border);
  background-color: var(--whitebg);
  position: sticky;
  top: 0;
  z-index: 500;
  display: flex;
  align-items: center;
  padding-left: 2rem;
}
.itemHolderAll {
  grid-column: 2 / 3;
  grid-row: 3 / 4;

  justify-content: center;

  height: 100%;
  width: 100%;
  flex: 1 1 0%;
}

.infoDesc {
  height: 100vh;
  width: 70%;
  min-width: 50rem;
  max-width: 60rem;
  position: sticky;
  top: 0;
  right: 0;
  flex: 1 1 0%;
  border-left: var(--border);
  z-index: 2000;
}
.errorsearch {
  text-align: center;
  min-width: 100%;
  color: var(--darkestgray);
  margin-top: 5rem;
}

@media screen and (min-width: 1600px) {
  .infoDesc {
    min-width: 80rem;
  }
}

@media screen and (max-width: 760px) {
  .infoDesc {
    min-width: 100vw;
    align-self: flex-start;
    position: fixed;
    margin-top: 5.5rem;
    left: 0;
    right: 0;
    border: none;
    z-index: 2000;
    overflow-x: hidden;
    overflow-y: scroll;
    margin-bottom: 20rem;
  }
}
</style>
