<template>
  <div id="logCon">
    <div v-for="each in store.logs" :key="each.id">
      <p id="log">
        {{ formatDateTime(each.dateTime) }} {{ each.change }}
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
 methods: {
 formatDateTime(dateTime) {
    if (!dateTime) return '';
    let [date, time] = dateTime.split('T');
    let newTime = time.split('.')[0];
    return `${date} ${newTime.replace('.', ':')}`;
 },
},
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
  margin-top: 1vw;
  font-size: 1vw;
}
</style>
