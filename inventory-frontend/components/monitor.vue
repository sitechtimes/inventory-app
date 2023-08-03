<template>
  <div class="bigdiv">
    <div id="mainItems">
      <div class="itemHeader subheading">Monitor</div>
      <div class="subheadorg">
        <div class="itemSub heading">Name</div>
        <div class="itemSub totalstock heading">Total Stock Available</div>
      </div>
    </div>

    <div class="itemHolderAll monitorHolder">
      <div class="categoryHolder search" v-if="store.search">
        <ItemPerCat
          v-for="(each, index) in store.items"
          :key="each.id"
          :list="each"
          :name="nameType(index)"
        ></ItemPerCat>
      </div>
      <div class="categoryHolder">
        <ItemPerCat
          v-for="(each, index) in store.items"
          :key="each.id"
          :list="each.itemsCategory"
          :name="store.nameType(index)"
        ></ItemPerCat>
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
      />
    </div>
  </div>
</template>

<script>
import ItemPerCat from "./itemPerCat.vue";
import Info from "./info.vue";
import { useItemsStore } from "~/store/ItemsStore";

export default {
  name: "Monitor",
  components: { ItemPerCat, Info },
  data() {
    return {
      store: useItemsStore(),
    };
  },
};
</script>

<style>
.monitorHolder {
  position: fixed;
  margin-top: 10rem;
}
.subheadorg {
  width: 100%;
  background-color: var(--whitebg);
  border-bottom: var(--border);
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.itemSub {
  padding: 1rem 2rem;
}
.totalstock {
  border-left: var(--border);
  max-width: 25rem;
  width: 20%;
  overflow: hidden;

  white-space: nowrap;
  text-overflow: ellipsis;
}
</style>
