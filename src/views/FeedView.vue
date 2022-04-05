<template>
  <!-- main feed page start -->
  <div
    class="feed wrapper container d-flex justify-content-center"
    style="background-color: #fafafa"
  >
    <div class="col-9">
      <div class="row">
        <div class="left col-8">
          <!-- stories start -->
          <div class="card">
            <div class="card-body d-flex justfy-content-start">
              <ul class="list-inline mb-0">
                <li class="list-inline-item align-conent-center">
                  <button class="btn p-0 m-0">
                    <div class="d-flex flex-column align-items-center">
                      <div
                        class="rounded-circle overflow-hidden d-flex justify-content-conter align-items-center border border-2 border-danger me-2 story-profile-photo"
                      >
                        <img
                          src="@/assets/cat1.jpg"
                          style="
                            transform: scale(1.5);
                            width: 100%;
                            position: absolute;
                            left: 0;
                          "
                        />
                      </div>
                      <small>cat1</small>
                    </div>
                  </button>
                </li>
              </ul>
            </div>
          </div>
          <!-- stories end -->

          <!-- feed start -->
          <FeedCard v-for="feed in latestFeeds" :key="feed.id" :feed="feed" />
        </div>
        <!-- feed end -->

        <!-- side-bar start -->
        <div class="right col-3 position-fixed" id="sidebar">
          <!-- side-profile start -->
          <div class="d-flex flex-row justify-content-between">
            <div class="d-flex flex-row align-items-center">
              <div
                class="rounded-circle overflow-hidden d-flex justify-content-center align-items-center border side-profile-photo me-3"
              >
                <img
                  src="@/assets/cat1.jpg"
                  style="
                    transform: scale(1.5);
                    width: 100%;
                    position: absolute;
                    left: 0;
                  "
                />
              </div>

              <div class="profile-info">
                <span class="profile-info-userid">coco</span>
                <span class="profile-info-name text-muted">chuchu</span>
              </div>
            </div>
            <button class="btn btn-primary btn-sm p-0 btn-ig">Switch</button>
          </div>

          <!-- side-profile end -->

          <!-- side-suggest start -->
          <div class="mt-4">
            <div class="d-flex flex-row justify-content-between">
              <small class="text-black-50 fw-bold mb-2"
                >Suggestions For You</small
              >
              <small>See All</small>
            </div>

            <div>
              <div class="d-flex flex-row justify-content-between">
                <div class="d-flex flex-row align-items-center">
                  <div
                    class="rounded-circle overflow-hidden d-flex justify-content-conter align-items-center border feed-profile-photo me-2"
                  >
                    <img
                      src="@/assets/cat2.jpg"
                      style="
                        transform: scale(1.5);
                        width: 100%;
                        position: absolute;
                        left: 0;
                      "
                    />
                  </div>
                  <strong>Instagram</strong>
                </div>
                <button class="btn btn-primary btn-sm p-0 btn-ig">
                  Follow
                </button>
              </div>
            </div>
          </div>
          <!-- side-suggest end -->
        </div>
        <!-- side-bar end -->
      </div>
    </div>
  </div>
  <!-- main feed page end -->
</template>

<script>
import FeedCard from "@/components/FeedCard.vue";

import axios from "axios";
export default {
  name: "FeedView",
  data() {
    return {
      latestFeeds: [],
    };
  },
  components: {
    FeedCard,
  },
  mounted() {
    this.getFeedList();
  },
  methods: {
    getFeedList() {
      axios.defaults.headers.common["Authorization"] =
        "Token " + localStorage.getItem("token");
      axios
        .get("http://127.0.0.1:8000/api/v1/")
        .then((response) => {
          this.latestFeeds = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style lang="css">
#sidebar {
  height: 100%;
  right: 170px;
}

.story-profile-photo {
  width: 56px;
  height: 56px;
  position: relative;
}

.feed-profile-photo {
  width: 46px;
  height: 46px;
  position: relative;
}

.btn-ig {
  background-color: transparent !important;
  border: 0 !important;
  color: #007bff !important;
  font-weight: 600;
  right: 0;
  bottom: 0;
  top: 0;
  outline: none !important;
}

.btn-ig:hover,
.btn-ig:focus {
  background-color: transparent !important;
  color: #007bff !important;
}

.comment-box {
  border-top: 0.1px solid lightgray;
}

.side-profile-photo {
  width: 56px;
  height: 56px;
  position: relative;
}

.profile-info-userid {
  display: block;
  font-size: 14px;
  font-weight: 700;
}

.profile-info-name {
  font-size: 12px;
}
</style>
