<template>
  <div>
    <div>
      <div
        class="subheading catHead"
        :class="store.monitor && 'monitorCatHead'"
        ref="cat"
        v-if="list.length > 0"
      >
        {{ name }}
      </div>
      <div class="itemHolder" v-if="store.catalog === true">
        <Item
          v-for="result in list"
          :key="result.id"
          :name="result.name"
          :quantity="result.total"
          :image="result.image_url"
          :updated="result.last_purchased"
          :vendor="result.vendor"
          :link="result.purchase_link"
          :category="result.category"
        />
      </div>
      <div class="itemHolder itemHolderM" v-if="store.monitor === true">
        <ItemMonitor
          v-for="result in list"
          :key="result.id"
          :name="result.name"
          :quantity="result.total"
          :image="result.image_url"
          :updated="result.last_purchased"
          :vendor="result.vendor"
          :link="result.purchase_link"
          :category="result.category"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Item from "./item.vue";
import { useItemsStore } from "~/store/ItemsStore";
import ItemMonitor from "./itemMonitor.vue";

export default {
  name: "ItemPerCat",
  props: { list: Array, name: String, min: Boolean },
  components: { Item, ItemMonitor },
  data() {
    return {
      store: useItemsStore(),
    };
  },
  methods: {},
  mounted() {
    this.store.cat.push(this.$refs.cat);
  },
};
</script>

<style>
.itemHolder {
  display: flex;
  height: fit-content;
  width: 100%;

  flex-direction: row;
  flex-wrap: wrap;
  align-items: stretch;
}
.catHead {
  padding-left: 2rem;
  padding-top: 1rem;
  padding-bottom: 1rem;
}
.monitorCatHead {
  border-bottom: var(--border);
  font-size: var(--h3);
}
.itemHolderM {
  flex-direction: column;
}
@media screen and (max-width: 1100px) {
  .info-cat {
    border-top: var(--border);
    border-bottom: var(--border);
  }
}
@media screen and (max-width: 760px) {
  .catHead {
    border-top: var(--border);
    border-bottom: var(--border);
  }
  .itemHolder {
    background-color: var(--whitebg);
  }
}
</style>
