<template>
  <div>
    <div class="open-menu-cont">
      <button class="open-menu-btn">
        <div
          v-if="dismiss === true"
          class="open-menu-icon-cont"
          @click="NavMenu"
        >
          <font-awesome-icon :icon="['fas', 'bars']" class="open-menu-icon" />
        </div>
        <div
          v-if="dismiss === false"
          class="open-menu-icon-cont"
          @click="NavMenu"
        >
          <font-awesome-icon
            :icon="['fas', 'xmark']"
            style="color: #000000"
            class="open-menu-icon"
          />
        </div>
      </button>
      <div class="mobile-menu dismiss">
        <div class="mobile-user">
          <div class="user-icon-cont">
            <font-awesome-icon
              :icon="['fas', 'user']"
              class="mobile-user-icon"
            />
          </div>
          <div class="mobile-user-info">
            <h2 class="mobile-user-title">My Account</h2>
            <h3 class="mobile-username">user1234@gmail.com</h3>
          </div>
        </div>
        <div class="mobile-menu-container">
          <button class="mobile-menu-btn">
            <div>
              <font-awesome-icon
                :icon="['fas', 'boxes-stacked']"
                class="mobile-icon"
              />
            </div>
            <h3 class="mobile-tag">Catalog</h3>
          </button>
          <button class="mobile-menu-btn">
            <div>
              <font-awesome-icon
                :icon="['fas', 'hand-holding-hand']"
                class="mobile-icon"
              />
            </div>
            <h3 class="mobile-tag">Borrowed</h3>
          </button>
          <button class="mobile-menu-btn">
            <div>
              <font-awesome-icon
                :icon="['fas', 'circle-exclamation']"
                class="mobile-icon"
              />
            </div>
            <h3 class="mobile-tag">Supplies Needed</h3>
          </button>
        </div>
      </div>
    </div>
    <!-- <div class="return-box" @click="NavMenu">
    </div> -->
    <div class="nav-cont">
      <div>
        <div class="user">
          <div class="user-icon-cont">
            <font-awesome-icon :icon="['fas', 'user']" class="user-icon" />
          </div>
          <!-- <div class="user-info">
            <h2 class="user-title">My Account</h2>
            <h3 class="username">user1234@gmail.com</h3>
          </div> -->
        </div>
        <div class="menu-container">
          <button class="menu-btn">
            <div>
              <font-awesome-icon
                :icon="['fas', 'boxes-stacked']"
                class="catalog-icon"
              />
            </div>
            <!-- <h3 class="tag">CATALOG</h3> -->
          </button>
          <button class="menu-btn">
            <div>
              <font-awesome-icon
                :icon="['fas', 'hand-holding-hand']"
                class="borrowed-icon"
              />
            </div>
            <!-- <h3 class="tag">BORROWED</h3> -->
          </button>
          <button class="menu-btn">
            <div>
              <font-awesome-icon
                :icon="['fas', 'circle-exclamation']"
                class="needed-icon"
              />
            </div>
            <!-- <h3 class="tag">SUPPLIES NEEDED</h3> -->
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserMenu",
  props: {},
  components: {},
  data() {
    return {
      dismiss: true,
    };
  },
  methods: {
    NavMenu() {
      const MobileMenu = document.querySelector(".mobile-menu");
      if (MobileMenu.classList.contains("selected")) {
        MobileMenu.classList.remove("selected");
        MobileMenu.classList.add("dismiss");
        this.dismiss = true;
        console.log("dismiss");
      } else if (MobileMenu.classList.contains("dismiss")) {
        MobileMenu.classList.remove("dismiss");
        this.dismiss = false;
        MobileMenu.classList.add("selected");
        console.log("selected");
      } else if (
        !MobileMenu.classList.contains("dismiss") ||
        !MobileMenu.classList.contains("selected")
      ) {
        MobileMenu.classList.add("selected");
        console.log("selected");
      }
    },
  },
};
</script>

<style scoped>
.nav-cont {
  height: 100vh;
  width: 18rem;

  display: flex;
  flex-flow: row;
}
.user {
  width: 6.9rem;
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-evenly;
  align-items: center;
  overflow: hidden;
  margin-top: 1rem;
}
.user-icon {
  width: 3rem;
  height: 3rem;
}

.menu-container {
  margin-top: 1rem;
  width: 100%;
  display: flex;
  flex-flow: column nowrap;
}

.menu-btn {
  padding: 1rem;
  width: 6.9rem;
  border: none;
  color: white;
  text-decoration: none;
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-evenly;
  align-items: center;
  transition: background-color 0.2s linear;
}

h2,
h3 {
  color: black;
  padding-left: 0.5rem;
  font-size: 0.6rem;
}
.menu-btn:hover {
  background-color: var(--lightblue);
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
  top: 0.7rem;
  left: 2rem;
  position: fixed;
  z-index: 900;
}
.open-menu-btn {
  width: 100%;
  height: 100%;
  border: none;
  background-color: transparent;
}
.open-menu-icon-cont {
  width: 100%;
  height: 100%;
}
.open-menu-icon {
  display: none;
}
.mobile-menu {
  display: none;
  flex-direction: column;
  position: relative;
  z-index: 10;
  background-color: white;
  width: 100vw;
  height: 100vh;
  overflow-x: hidden;
  overflow-y: hidden;
}
.mobile-menu-btn,
.mobile-user {
  display: grid;
  grid-template-columns: 4rem 1fr;
  grid-template-rows: 4rem 1fr;
  margin-top: 3vh;
  padding-top: 2vh;
  padding-bottom: 2vh;
  width: 100%;
  height: 8vh;
  text-decoration: none;
  background-color: white;
}

.mobile-user-icon,
.mobile-icon {
  display: grid;
  color: #c7d6d5;
  width: 5rem;
  height: 5rem;
}
.mobile-user-icon {
  color: black;
}
.mobile-user-info,
.mobile-tag {
  display: grid;
  color: black;
  font-size: 4rem;
}
.mobile-user {
  background-color: white;
  display: grid;
  flex-flow: row nowrap;
  align-items: center;
  margin-top: 0.8vh;
  padding-top: 2.5vh;
  height: 10vh;
  justify-self: center;
}
.mobile-user-title,
.mobile-username {
  font-size: 2rem;
  display: flex;
  flex-flow: column;
  align-items: center;
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
    -webkit-transform: translateX(0%);
    transform: translateX(0%);
  }
  100% {
    -webkit-transform: translateX(-500%);
    transform: translateX(-500%);
  }
}
@-webkit-keyframes slide-out {
  0% {
    -webkit-transform: translateX(0%);
    transform: translateX(0%);
  }
  100% {
    -webkit-transform: translateX(-500%);
    transform: translateX(-500%);
  }
}
@keyframes slide-in {
  0% {
    -webkit-transform: translateX(-500%);
    transform: translateX(-500%);
  }
  100% {
    -webkit-transform: translateX(0%);
    transform: translateX(0%);
  }
}
@-webkit-keyframes slide-in {
  0% {
    -webkit-transform: translateX(-500%);
    transform: translateX(-500%);
  }
  100% {
    -webkit-transform: translateX(0%);
    transform: translateX(0%);
  }
}

/* media query */
/* media queries max width
    sm:	 ≥576px
 	  md:  ≥768px
    lg:	 ≥992px
    xl:  ≥1200px
    xxl: ≥1400px
*/

/* mobile */
@media (hover: hover) {
  .mobile-menu-btn:hover {
    background-color: var(--lightblue);
    cursor: pointer;
  }
}
@media screen and (max-width: 1200px) {
}
@media screen and (max-width: 576px) {
  .nav-cont {
    display: none;
  }
  .open-menu-cont {
    display: block;
  }
  .open-menu-icon {
    height: 200%;
    width: 200%;
    display: block;
  }
  .mobile-menu {
    display: flex;
    margin-top: 140%;
  }
  .mobile-icon {
    height: 4rem;
    width: 4rem;
  }
  .mobile-tag {
    font-size: 3rem;
  }
}
@media screen and (max-width: 375px) {
  .nav-cont {
    display: none;
  }
  .open-menu-cont {
    display: block;
  }
  .open-menu-icon {
    height: 200%;
    width: 200%;
    display: block;
  }
  .mobile-icon {
    height: 3.5rem;
    width: 3.5rem;
  }
  .mobile-tag {
    font-size: 2.5rem;
  }
}
@media screen and (max-width: 320px) {
  .nav-cont {
    display: none;
  }
  .open-menu-cont {
    display: block;
  }
  .open-menu-icon {
    height: 200%;
    width: 200%;
    display: block;
  }
  .mobile-user-icon {
    height: 4rem;
    width: 4rem;
  }
  .mobile-icon {
    height: 3rem;
    width: 3rem;
  }
  .mobile-tag {
    font-size: 2rem;
  }
}
</style>
