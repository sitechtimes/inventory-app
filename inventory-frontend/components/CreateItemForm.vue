<template>
  <div>
    <form action="">
      <div class="cont">
        <div class="Textcont">
          <div class="cont1">
            <div class="itemName">
              <input type="text" name="name" placeholder="Enter the Name of the Item" class="nameText" />
            </div>
            <div class="quantity-cont">
              <input id="quantity" type="number" name="makerspace" placeholder="Maker Space Quantity">
              <input id="quantity" type="number" name="backrrom" placeholder="Back Room Quantity">
            </div>
          </div>


          <div class="cont2">
            <div>
              <input id="location" type="text" name="location" placeholder="Enter the location of the Item" />

            </div>
            <div>
              <select name="Vendor" id="">
                <option value="">Choose a Vendor</option>
                <option value="DOE">ShopDOE</option>
                <option value="AMZ">Amazon</option>
                <option value="BLICK">Blick</option>
                <option value="HD">Home Depot</option>
              </select>
              <select name="Category" id="">
                <option value="">Choose a Category</option>
                <option value="TLS">Tools</option>
                <option value="PT">Paint</option>
                <option value="TP">Tape</option>
                <option value="WR">Wire</option>
                <option value="FA">First Aid</option>
                <option value="Fabric">Fabric</option>
                <option value="Paper Mache">Paper Mache</option>
                <option value="Glue">Glue</option>
                <option value="Sewing">Sewing</option>
                <option value="Miscellaneous">Miscellaneous</option>
                <option value="Coloring Materials">Coloring Materials</option>
                <option value="Sculpture">Sculpture</option>
                <option value="Wood">Wood</option>
                <option value="Craft Supplies">Craft Supplies</option>
                <option value="Foam">Foam</option>
                <option value="Printmaking">Printmaking</option>
                <option value="Paper">Paper</option>
                <option value="Drawing">Drawing</option>
              </select>

            </div>

          </div>

        </div>


        <div class="imagecont">



          <div class="preview">
            <img src="" alt="" id="preview-selected-image">
          </div>
          <input id="imageInput" type="file" name="imageinput" accept="image/*" @change="previewImage" />
        </div>
      </div>

      <input type="submit">
    </form>
  </div>
</template>

<script setup>
function previewImage(event) {
  const imageFiles = event.target.files;
  const imageFilesLength = imageFiles.length;

  if (imageFilesLength > 0) {
    const imageSrc = URL.createObjectURL(imageFiles[0]);
    const imagePreviewElement = document.querySelector("#preview-selected-image");
    imagePreviewElement.src = imageSrc;
    imagePreviewElement.style.display = "block";
  }
};
</script>

<style scoped>
form {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 80rem;
  height: 60rem;
  background-color: red;
  border-radius: 0.5rem;
  display: flex;
  justify-content: center;
  align-items: center;
}

input {
  height: 5rem;
  font-size: 1.5rem;
  margin-bottom: .5rem;
}

option {
  font-size: 1.5rem;

}

select {
  height: 5rem;
  font-size: 1.5rem;
  width: 30rem;
  margin-bottom: .5rem;
}


.cont {
  width: 90%;
  height: 90%;
  background-color: green;
  display: flex;
  flex-flow: row nowrap;
}

.Textcont {
  width: 50%;
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  align-items: center;
}

.cont1 {
  display: flex;
  flex-flow: column wrap;
  justify-content: space-between;
}

.nameText {
  width: 30rem;
}

.quantity-cont {
  display: flex;
  flex-flow: row nowrap;
}

#quantity {
  width: 15rem;

}

.cont2 {
  display: flex;
  flex-flow: column wrap;
  justify-content: space-between;
  width: 30rem;
}

#location {
  width: 30rem;
}

.imagecont {
  display: flex;
  flex-flow: column nowrap;
  align-items: center;
  width: 50%;
}

.imageLabel {
  font-size: 2rem;

}

#imageInput {
  margin: auto;
  width: 20rem;
}

.preview {
  border: dotted;
  width: 100%;
  height: 65%;
  border-radius: 1rem;
}
</style>
