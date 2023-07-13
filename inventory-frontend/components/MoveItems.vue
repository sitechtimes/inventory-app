<template>
  <div class="change">
    <div class="location">
      <h2>Makerspace</h2>
      <h2>Back Room</h2>
    </div>
    <div class="amount">
      <h3>{{ Makerspace }}</h3>
      <h3>{{ Backroom }}</h3>
    </div>
    <div v-if="haveSupplies" class="error">
      <h2>None left in {{ room }}</h2>
    </div>
    <div class="btn">
      <button @click="toMakerspace"></button>
      <button @click="toBackRoom"></button>
    </div>
  </div>
</template>

<script setup>
let Makerspace = ref(2);
let Backroom = ref(0);
let haveSupplies = ref(false);
let room = ref("");

function toBackRoom() {
  if (Makerspace.value > 0) {
    room.value = "";
    haveSupplies.value = false;
    Backroom.value += 1;
    Makerspace.value -= 1;
  } else {
    room.value = "Makerspace";
    haveSupplies.value = true;
  }
}

function toMakerspace() {
  if (Backroom.value > 0) {
    room.value = "";
    haveSupplies.value = false;

    Makerspace.value += 1;
    Backroom.value -= 1;
  } else {
    room.value = "Backroom";
    haveSupplies.value = true;
  }
}
</script>

<style scoped>
.change {
  border: solid 1px black;
  width: 20rem;
  height: 10rem;
  display: flex;
  flex-flow: column nowrap;
}
.location,
.amount,
.btn {
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-evenly;
  align-items: center;
}
.amount {
  height: 3rem;
}
button {
  border: none;
  width: 5rem;
  height: 2.5rem;
}
</style>
