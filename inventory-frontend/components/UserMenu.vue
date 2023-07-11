<template>
  <div>
    <div class="open-menu-cont">
      <button class="open-menu-btn" @click="NavMenu()">
        <div class="open-menu-icon-cont">
          <font-awesome-icon :icon="['fas', 'bars']" class="open-menu-icon" />
        </div>
      </button>
    </div>
    <div class="nav-cont">
      <div>
        <div class="user">
          <div class="user-icon-cont">
            <font-awesome-icon :icon="['fas', 'user']" class="user-icon" />
          </div>
          <div class="user-info">
            <h2 class="user-title">My Account</h2>
            <h3 class="username">user1234@gmail.com</h3>
          </div>
        </div>
        <div class="menu-container">
          <button class="menu-btn">
            <div>
              <font-awesome-icon
                :icon="['fas', 'boxes-stacked']"
                class="catalog-icon"
              />
            </div>
            <h3 class="tag">CATALOG</h3>
          </button>
          <button class="menu-btn">
            <div>
              <font-awesome-icon
                :icon="['fas', 'hand-holding-hand']"
                class="borrowed-icon"
              />
            </div>
            <h3 class="tag">BORROWED</h3>
          </button>
          <button class="menu-btn">
            <div>
              <font-awesome-icon
                :icon="['fas', 'circle-exclamation']"
                class="needed-icon"
              />
            </div>
            <h3 class="tag">SUPPLIES NEEDED</h3>
          </button>
        </div>
      </div>
      <div class="back-cont">
        <button class="back-btn" @click="NavMenu()">
          <div class="back-icon">
            <font-awesome-icon :icon="['fas', 'angles-left']" />
          </div>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
let NavCont = "";
onMounted(() => {
  NavCont = document.querySelector(".nav-cont");
});

function NavMenu() {
  console.log(NavCont);
  if (NavCont.classList.contains("selected")) {
    NavCont.classList.remove("selected");
    NavCont.classList.add("dismiss");
    console.log("dismiss");
  } else if (NavCont.classList.contains("dismiss")) {
    NavCont.classList.remove("dismiss");
    NavCont.classList.add("selected");
    console.log("selected");
  } else if (
    !NavCont.classList.contains("dismiss") ||
    !NavCont.classList.contains("selected")
  ) {
    NavCont.classList.add("selected");
    console.log("selected");
  }
}
</script>

<style scoped>
.nav-cont {
  position: absolute;
  top: 0%;
  left: 0%;
  height: 100vh;
  width: 20.5 rem;
  background-color: #6d7275;
  display: flex;
  flex-flow: row;
}

.back-cont {
  display: none;
  width: 1.5rem;
  height: 100%;
}
.back-btn {
  border: none;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #c7d6d5;
}

.icon {
  width: 90%;
  height: 90%;
}
.user {
  width: 100%;
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-evenly;
  align-items: center;
  overflow: hidden;
}
.user-title {
  color: #ecebf3;
}
.username {
  color: #ecebf3;
}
.user-icon-cont {
  width: 4rem;
  height: 4rem;
  display: flex;
  align-content: center;
  justify-content: center;
}
.user-icon {
  width: 80%;
  height: 80%;
}

.user-info {
  margin-left: 1rem;
  width: 14rem;
  overflow: hidden;
}
.menu-container {
  width: 100%;
  display: flex;
  flex-flow: column nowrap;
}
.tag {
  width: 14rem;
}
.menu-icon {
  width: 1rem;
  height: 1rem;
  background-color: #6d7275;
  border-radius: 2rem;
}
.menu-btn {
  padding: 1rem;
  width: 100%;
  border: none;
  background-color: #6d7275;
  color: white;
  text-decoration: none;
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-evenly;
  align-items: center;
  transition: background-color 0.2s linear;
}
.menu-btn:hover {
  background-color: #ecebf3;
}
.catalog-icon,
.borrowed-icon,
.needed-icon {
  color: #c7d6d5;
  width: 2rem;
  height: 2rem;
}
.open-menu-cont {
  display: none;
  width: 2rem;
  height: 2rem;
}
.open-menu-btn {
  width: 100%;
  height: 100%;
}
.open-menu-btn {
  border: none;
  background-color: transparent;
}
.open-menu-icon-cont {
  width: 100%;
  height: 100%;
}
.open-menu-icon {
  width: 100%;
  height: 100%;
}
/* animations  */
.selected {
  animation: slide-in 0.5s forwards;
  -webkit-animation: slide-in 0.5s forwards;
}

.dismiss {
  animation: slide-out 0.5s forwards;
  -webkit-animation: slide-out 0.5s forwards;
}
@keyframes slide-out {
  0% {
    transform: translateX(0%);
  }
  100% {
    transform: translateX(-100%);
  }
}
@keyframes slide-in {
  0% {
    -webkit-transform: translateX(-100%);
  }
  100% {
    -webkit-transform: translateX(0%);
  }
}
/* media query */
/* mobile */
@media (max-width: 1200px) {
  .back-cont {
    display: block;
  }
  .nav-cont {
    transform: translateX(-100%);
  }
  .open-menu-cont {
    display: block;
  }
}
</style>
