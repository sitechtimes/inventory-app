<template>
  <div>
    <div>
      <div class="subheading catHead">{{ name }}</div>
      <div class="itemHolder">
        <Item
          v-for="result in list"
          :key="result.id"
          :name="result.name"
          :quantity="result.quantity"
          :image="result.image"
          :available="true"
          :updated="result.last_purchased"
          :vendor="result.vendor"
          :link="result.purchase_link"
          :category="result.category"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
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
@media screen and (max-width: 760px) {
  .catHead {
    border-top: solid 1px var(--darkgray);
    border-bottom: solid 1px var(--darkgray);
  }
  .itemHolder {
    background-color: var(--whitebg);
  }
}
</style>

<script>
import Item from "./item.vue";

export default {
  name: "ItemPerCat",
  props: { list: Array, name: String },
  components: { Item },
};
</script>
