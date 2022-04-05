<template>
  <!-- Modal -->
  <div
    class="modal fade"
    id="exampleModal"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header d-flex justify-content-center">
          <h5 class="modal-title" id="exampleModalLabel">Create new post</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <input
                type="file"
                name="postImage"
                id="postImage"
                ref="postImage"
                @change="imageUpload"
              />
            </div>
            <div>
              <textarea
                class="mb-3"
                name="description"
                id="description"
                cols="40"
                rows="10"
                v-model="form.description"
              ></textarea>
            </div>
            <button
              type="submit"
              class="btn btn-primary mb-3"
              @click="submitForm"
            >
              submit
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "PostModal",
  data() {
    return {
      form: {
        description: "",
        image: "",
      },
      errors: [],
    };
  },
  methods: {
    submitForm() {
      this.errors = [];

      const formdata = new FormData();
      formdata.append("description", this.form.description);
      formdata.append("image", this.form.image);

      const config = {
        headers: {
          "content-Type": "multipart/form-data",
          Authorization: "Token " + localStorage.getItem("token"),
        },
      };

      axios
        .post("http://127.0.0.1:8000/api/v1/", formdata, config)
        .then((res) => {
          console.log("POST WORK");
          console.log(res);
        })
        .catch((error) => {
          this.error.push(error);
        });
    },
    imageUpload() {
      this.form.image = this.$refs.postImage.files[0];
    },
  },
};
</script>

<style></style>
