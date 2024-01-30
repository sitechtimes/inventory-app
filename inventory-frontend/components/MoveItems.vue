<template>
  <div class="change">
    <div class="change-btn">
      <button v-if="!edit" @click="edit = true" class="edit-btn">
        <font-awesome-icon :icon="['fas', 'pen-to-square']" />
      </button>
      <button v-if="edit" @click="manualEdit()" class="save-btn">
        <font-awesome-icon :icon="['fas', 'floppy-disk']" />
      </button>
    </div>
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
      <button v-if="!edit" @click="toMakerspace()">
        <font-awesome-icon :icon="['fas', 'angles-left']" />
      </button>
      <button v-if="!edit" @click="toBackRoom()">
        <font-awesome-icon :icon="['fas', 'angles-right']" />
      </button>
    </div>
  </div>
</template>

<script setup>
const props = defineProps(["id"]);
let Makerspace = ref(0);
let Backroom = ref(0);
let haveSupplies = ref(false);
let room = ref("");
let edit = ref(false);
onMounted(() => {
  watch(
    () => props.id,
    () => {
      item();
    },
    { immediate: true }
  );
});

function item() {

  const config = useRuntimeConfig()
  $fetch(`${config.public.protocol}://${config.public.baseurl}:${config.public.port}/items/items/CurrentItem/${props.id}/`, {

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
    .then((response) => {
      Makerspace.value = response.makerspace_quantity;
      Backroom.value = response.backroom_quantity;
    })
    .catch((error) => console.log(error));
}

function toBackRoom() {
  room.value = "";
  haveSupplies.value = false;
  const config = useRuntimeConfig()
  $fetch(`${config.public.protocol}://${config.public.baseurl}:${config.public.port}/items/updateQuantity/${props.id}/makerspace/`, {

    method: "PUT",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    referrerPolicy: "no-referrer",
  })
    .then((response) => {
      console.log(response);
      Backroom.value += 1;
      Makerspace.value -= 1;
    })
    .catch((error) => {
      console.log(error);
      room.value = "Makerspace";
      haveSupplies.value = true;
    });
}

function toMakerspace() {
  room.value = "";
  haveSupplies.value = false;
  const config = useRuntimeConfig()
  $fetch(`${config.public.protocol}://${config.public.baseurl}:${config.public.port}/items/updateQuantity/${props.id}/backroom/`, {

    method: "PUT",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    referrerPolicy: "no-referrer",
  })
    .then((response) => {
      console.log(response);
      Makerspace.value += 1;
      Backroom.value -= 1;
    })
    .catch((error) => {
      console.log(error);
      room.value = "Backroom";
      haveSupplies.value = true;
    });
}

function manualEdit() {
  if (Makerspace.value > 0 && Backroom.value > 0) {
    const config = useRuntimeConfig()
    fetch(
      `${config.public.protocol}://${config.public.baseurl}:${config.public.port}/items/updateQuantity/manual/${props.id}/${Makerspace.value}/${Backroom.value}/`,

      {
        method: "PUT",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
      }
    )
      .then((response) => {
        console.log(response);
        edit.value = false;
      })
      .catch((error) => {
        console.log(error);
      });
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
.location {
  height: 3rem;
}
.amount {
  height: 3rem;
}

button {
  border: none;
  width: 5rem;
  height: 2.5rem;
}

input {
  text-align: center;
  width: 38%;
  height: 2rem;
  margin: 1rem;
}

.change-btn {
  height: 1rem;
  display: flex;
  flex-flow: row nowrap;
  justify-content: flex-end;
}
.edit-btn,
.save-btn {
  position: relative;
  top: 0;
  right: 0;
  width: 1.5rem;
  height: 1.5rem;
  background: none;
}
</style>
