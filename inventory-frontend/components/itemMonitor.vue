<template>
  <div class="itemMonitor" ref="main" @mousedown="clickedMonitor">
    <div class="nameM text" ref="name">{{ name }}</div>
    <div class="quantityM smalltext" ref="quant">{{ quantity }} 2</div>
  </div>
</template>

<script>
export default {
  name: "ItemMonitor",
  props: {
    name: String,
    quantity: Number,
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
  max-width: 70%;
}
.quantityM {
  max-width: 25rem;
  width: 20%;
  height: 100%;

  padding: 1rem;
}
.itemMonitor {
  background-color: var(--whitebg);
  border-bottom: var(--border);
  display: flex;
  align-items: center;
  width: 95%;
  justify-content: space-between;
}
</style>
