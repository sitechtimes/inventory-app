<template>
  <div v-if="showNotification" class="fade-div" id="notification">
    <div class="noti">
      <p>You have successfully added {{ num }} {{ name }}</p>
    </div>
  </div>
</template>

<script>
import {
  showNotification,
  notiItemName,
  notiItemAmt,
} from "../assets/globalVar.js";

export default {
  data() {
    return {
      showNotification: showNotification,
      name: notiItemName,
      num: notiItemAmt,
    };
  },
};
</script>

<style>
.noti {
  position: absolute;
  background-color: rgb(166, 223, 166);
  padding: 1vw;
  font-size: 1.2vw;
  left: 50%;
  transform: translate(-50%, 0);
  z-index: 501;
  border-radius: 1000px;
}
@keyframes fadeAnimation {
  0%,
  100% {
    opacity: 0;
    z-index: 9999;
  }
  25%,
  75% {
    top: 1vw;
    opacity: 1;
    z-index: 9999;
  }
}

.fade-div {
  top: 1vw;
  position: absolute;
  left: 50%;
  transform: translate(-50%, 0);
  z-index: 501;
  animation: fadeAnimation 2s;
  animation-iteration-count: 1;
  width: 50vw;
  height: auto;
  animation-fill-mode: forwards;
}
</style>
