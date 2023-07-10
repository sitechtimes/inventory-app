<template>
  <div class="nav-cont">
    <div class="user">
      <div class="user-photo-cont">
        <div class="user-icon"></div>
      </div>
      <div class="user-info">
        <h2 class="user-title">My Account</h2>
        <h3 class="username">user1234@gmail.com</h3>
      </div>
    </div>
    <div class="menu-container">
      <button class="catalog">
        <div class="catalog-icon"></div>
        <h3 class="tag">CATALOG</h3>
      </button>
      <button class="items-borrowed">
        <div class="borrow-icon"></div>
        <h3 class="tag">BORROWED</h3>
      </button>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
.nav-cont {
  position: absolute;
  top: 0%;
  left: 0%;
  height: 100vh;
  width: 20rem;
  background-color: #0c120c;
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
.user-photo-cont {
  width: 4rem;
  height: 4rem;
}
.user-icon {
  width: 100%;
  height: 100%;
  background-color: white;
  border-radius: 2rem;
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
.catalog-icon {
  width: 1rem;
  height: 1rem;
  background-color: #0c120c;
  border-radius: 2rem;
}
.borrow-icon {
  width: 1rem;
  height: 1rem;
  background-color: #0c120c;
  border-radius: 2rem;
}
.catalog {
  padding: 1rem;
  width: 100%;
  border: none;
  background-color: #0c120c;
  color: white;
  text-decoration: none;
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-evenly;
  align-items: center;
  transition: background-color 0.2s linear;
}
.items-borrowed {
  padding: 1rem;
  width: 100%;
  border: none;
  background-color: #0c120c;
  color: white;
  text-decoration: none;
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-evenly;
  align-items: center;
  transition: background-color 0.2s linear;
}
.items-borrowed:hover {
  background-color: #6d7275;
}
.catalog:hover {
  background-color: #6d7275;
}
</style>
