<template>
  <div id="logCon">
    <div v-for="each in store.logs" :key="each.id">
      <p id="log">
        {{ each.pub_date }} {{ each.name }} {{ each.category }}
        {{ each.backroom_quantity }} {{ each.makerspace_quantity }}
        {{ each.purchase_link }}
        {{ each.vendor }}
      </p>
    </div>
  </div>
</template>
<script>
import { useItemsStore } from "~/store/ItemsStore";
export default {
  name: "InvLog",
  props: { list: Array, name: String },
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
#logCon {
  margin-left: 1vw;
  margin-top: 1vw;
}
#log {
  font-size: 1vw;
}
</style>
