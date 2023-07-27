<template>
  <div>
    <form action="" @submit.prevent="submitForm()">
      <div class="biggerCont">
        <div class="Textcont">
          <div class="cont1">
            <div class="itemName">
              <input id="name" type="text" placeholder="Enter the Name of the Item" class="nameText" required />
            </div>
            <div class="quantity-cont">
              <input id="quantity-makerspace" type="number" placeholder="Maker Space Quantity" required>
              <input id="quantity-backroom" type="number" placeholder="Back Room Quantity" required>
            </div>
          </div>
          <div class="cont2">
            <div>
              <input id="location" type="text" placeholder="Enter the location of the Item" required />
            </div>
            <div>
              <select name="Vendor" id="Vendor" required>
                <option value="">Choose a Vendor</option>
                <option value="DOE">ShopDOE</option>
                <option value="AMZ">Amazon</option>
                <option value="BLICK">Blick</option>
                <option value="HD">Home Depot</option>
              </select>
              <select name="Category" id="Category" required>
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
            <input type="file" id="actual-btn" accept="image/*" @change="previewImage" hidden required />
            <label class="imageLabel" for="actual-btn">Choose Image File</label>
          </div>
          <div class="addPhotoBtn">

          </div>
        </div>
      </div>
      <div class="submitCont">
        <input id="submitBtn" type="submit">
      </div>
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
    const imageLabelElement = document.querySelector(".imageLabel");
    imageLabelElement.style.opacity = 0;
    imagePreviewElement.src = imageSrc;
    imagePreviewElement.style.display = "block";
  }
};

function submitForm() {

  let name = document.getElementById("name").value;
  let makerspace = document.getElementById("quantity-makerspace").value;
  let backroom = document.getElementById("quantity-backroom").value;
  let location = document.getElementById("location").value;
  let Vendor = document.getElementById("Vendor").value;
  let Category = document.getElementById("Category").value;
  let image = document.getElementById("preview-selected-image").src;

  const formData = new FormData();
  formData.append("image", image);
  formData.append("name", name);
  formData.append("makerspace", makerspace);
  formData.append("backroom", backroom);
  formData.append("location", location);
  formData.append("Vendor", Vendor);
  formData.append("Category", Category);

  fetch("http://127.0.0.1:8000/items/addItems/", {
    method: "POST",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    referrerPolicy: "no-referrer",
    body: formData
  }).then((response) => {
    console.log(response)
  });
}
</script>

<style scoped>
form {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 80rem;
  height: 50rem;
  background-color: rgb(221, 221, 221);
  border-radius: 0.5rem;
  display: flex;
  flex-flow: column nowrap;
}

.biggerCont {
  display: flex;
  flex-flow: row now;
  height: 44rem;

}

input {

  height: 6rem;
  font-size: 1.6rem;
  margin-bottom: .8rem;
}

option {
  font-size: 1.6rem;
}

select {
  height: 6rem;
  font-size: 1.6rem;
  width: 30rem;
  margin-bottom: .8rem;
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

#quantity-makerspace,
#quantity-backroom {
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
  justify-content: center;
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
  border: solid 0.2px;
  width: 32rem;
  height: 32rem;
  border-radius: 1.2rem;
  display: flex;
  justify-content: center;
  margin-bottom: 2rem;
}

#imageInput {
  position: absolute;
  transform: translate(-50%, -50%);
  display: none;
  width: 5rem;
  height: 2rem;
}

#preview-selected-image {
  width: 100%;
  height: 100%;
}

.imageLabel {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  width: 29rem;
  height: 28rem;
  color: white;
  padding: 0.5rem;
  font-family: sans-serif;
  border-radius: 0.3rem;
  cursor: pointer;
  margin-top: 1rem;
}

.submitCont {
  display: flex;
  justify-content: center;
}

#submitBtn {
  width: 12rem;
  height: 4rem;
  background-color: rgb(195, 206, 206);
  border: solid 1px;
  border-radius: .5rem;
}
</style>
