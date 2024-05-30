<template>
  <div class="notifs">
    <div v-if="store.alerts === 0" class="heading noNotif">
      No Notifications
    </div>
    <div class="alerts-cont" v-else>
      <div class="text alertTotal">{{ store.alerts }} Notifications</div>
      <div
        class="alerts-indiv"
        v-for="each in store.alerted_items"
        :key="each.name"
      >
        <div class="text">
          <span class="text varText">
            {{ each.quantity }}
          </span>
          left of
          <span class="text varText">{{ each.name }} </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { onMounted } from 'vue';
import { useItemsStore } from "~/store/ItemsStore";
export default {
  name: "Alerts",
  data() {
    return {
      store: useItemsStore(),
    };
  },
  onMounted(){
    console.log(store)
  }
};

</script>

<style>
.alertTotal {
  margin-bottom: 1rem;
  margin-left: 0.5rem;
  color: rgb(201, 37, 86);
}
.notifs {
  padding: 2rem 1rem;
  height: fit-content;
  max-height: 50%;
  width: 30rem;
  border: var(--border);
  position: fixed;
  right: 0;
  top: 5.5rem;
  background-color: var(--whitebg);
  z-index: 60000;
  box-shadow: 0.2rem 0.2rem 0.5rem var(--tpdarkgray);
  overflow-y: scroll;
}

.alerts-indiv {
  padding: 0.5rem 0.5rem 1rem 0.5rem;
}
.noNotif,
.varText {
  color: var(--darkestgray);
}
</style>
