<template>
  <div>
    <form action="">
      <input type="text" name="name" />
      <label for="name">Item Name</label>
      <div class="img-cont">
        <input type="file" name="itemImg" />
        <label for="itemImg">Insert Image File Here</label>
      </div>
      <div class="text-cont">
        <input type="number" name="quantity" />
        <label for="quantity">Quantity</label>

        <label for="category">Choose the Category</label>
        <input type="text" name="purchase-link" />
        <label for="purchase-link">Purchase Link</label>
      </div>
      <div class="options">
        <select name="vendor" id="">
          <option value="">Select Vendor</option>
          <option value="DOE">ShopDoe</option>
          <option value="AMZ">Amazon</option>
          <option value="BLICK">Blick</option>
          <option value="HD">Home Depot</option>
        </select>
        <select name="category" id="">
          <option value="">Select Category</option>
          <option value="TLS">Tools</option>
          <option value="PT">Paint</option>
          <option value="TP">Tape</option>
          <option value="WR">Wire</option>
          <option value="FA">First Aid</option>
          <option value="FAB">Fabric</option>
          <option value="PM">Paper Mache</option>
          <option value="GL">Glue</option>
          <option value="SE">Sewing</option>
          <option value="MISC">Miscellaneous</option>
          <option value="CM">Coloring Materials</option>
          <option value="SC">Sculpture</option>
          <option value="WD">Wood</option>
        </select>
        <select name="location" id="">
          <option value="">Select Location</option>
          <option value="MS">Maker Space</option>
          <option value="BR">Back Room</option>
        </select>
      </div>
    </form>
  </div>
</template>

<script setup>
const category = [];
</script>

<style lang="scss" scoped></style>
