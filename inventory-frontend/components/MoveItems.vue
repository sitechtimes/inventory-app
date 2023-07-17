<template>
  <div class="change">
    <div class="location">
      <h2>Makerspace</h2>
      <h2>Back Room</h2>
    </div>
    <div class="amount">
      <input v-if="edit" v-model="Makerspace" />
      <input v-if="edit" v-model="Backroom" />
      <h3 v-if="!edit">{{ Makerspace }}</h3>
      <h3 v-if="!edit">{{ Backroom }}</h3>
    </div>
    <div v-if="haveSupplies" class="error">
      <h2>None left in {{ room }}</h2>
    </div>
    <div class="btn">
      <button @click="toMakerspace"></button>
      <button @click="toBackRoom"></button>
    </div>
    <div class="change-btn">
      <button v-if="!edit" @click="edit = true">
        <font-awesome-icon :icon="['fas', 'pen-to-square']" />
      </button>
      <button v-if="edit" @click="edit = false">
        <font-awesome-icon :icon="['fas', 'floppy-disk']" />
      </button>
    </div>
  </div>
</template>

<script setup>
let Makerspace = ref(2);
let Backroom = ref(0);
let haveSupplies = ref(false);
let room = ref("");
let edit = ref(false);

onMounted(() => {
  $fetch("http://127.0.0.1:8000/items/category/", {
    method: "GET",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    referrerPolicy: "no-referrer",
  })
    .then((response) => console.log(response))
    .catch((error) => console.log(error));
});
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
