<template>
  <!-- main feed page start -->
  <div
    class="feed wrapper container d-flex justify-content-center mt-5 pt-5"
    style="background-color: #fafafa"
  >
    <div class="col-9">
      <div class="row">
        <div class="left col-8">
          <!-- stories start -->
          <div class="card">
            <div class="card-body d-flex justfy-content-start">
              <ul class="list-inline mb-0">
                <list class="list-inline-iten">
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
                </list>
              </ul>
            </div>
          </div>
          <!-- stories end -->

          <!-- feed start -->
          <div class="d-flex flex-column mt-4 mb-4">
            <div class="card">
              <!-- feed-header start -->
              <div class="card-header bg-white">
                <div class="d-flex flex-row align-items-center">
                  <div
                    class="rounded-circle overflow-hidden d-flex justify-content-center align-items-center border border-2 border-danger me-3 feed-profile-photo"
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
                  <span class="fw-bold">cat1</span>
                </div>
              </div>
              <!-- feed-header end -->

              <!-- feed-body start -->
              <div class="card-body p-0">
                <!-- feed-body-image start -->
                <div class="ratio" style="--bs-aspect-ratio: 125%">
                  <img src="@/assets/image/summer-jacket2.jpg" alt="photo" />
                </div>
                <!-- feed-body-image end -->

                <!-- feed-body-menubar start -->
                <div class="d-flex justify-content-between ps-3 pe-3 pt-3 pb-1">
                  <ul class="list-inline mb-0">
                    <li class="list-inline-item">
                      <button class="btn p-0">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="1.6em"
                          height="1.6em"
                          fill="currentColor"
                          class="bi bi-heart"
                          viewBox="0 0 16 16"
                        >
                          <path
                            d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"
                          />
                        </svg>
                      </button>
                    </li>
                    <li class="list-inline-item ms-2">
                      <button class="btn p-0">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="1.6em"
                          height="1.6em"
                          fill="currentColor"
                          class="bi bi-chat"
                          viewBox="0 0 16 16"
                        >
                          <path
                            d="M2.678 11.894a1 1 0 0 1 .287.801 10.97 10.97 0 0 1-.398 2c1.395-.323 2.247-.697 2.634-.893a1 1 0 0 1 .71-.074A8.06 8.06 0 0 0 8 14c3.996 0 7-2.807 7-6 0-3.192-3.004-6-7-6S1 4.808 1 8c0 1.468.617 2.83 1.678 3.894zm-.493 3.905a21.682 21.682 0 0 1-.713.129c-.2.032-.352-.176-.273-.362a9.68 9.68 0 0 0 .244-.637l.003-.01c.248-.72.45-1.548.524-2.319C.743 11.37 0 9.76 0 8c0-3.866 3.582-7 8-7s8 3.134 8 7-3.582 7-8 7a9.06 9.06 0 0 1-2.347-.306c-.52.263-1.639.742-3.468 1.105z"
                          />
                        </svg>
                      </button>
                    </li>
                    <li class="list-inline-item ms-2">
                      <button class="btn p-0">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="1.6em"
                          height="1.6em"
                          fill="currentColor"
                          class="bi bi-send"
                          viewBox="0 0 16 16"
                        >
                          <path
                            d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576 6.636 10.07Zm6.787-8.201L1.591 6.602l4.339 2.76 7.494-7.493Z"
                          />
                        </svg>
                      </button>
                    </li>
                  </ul>
                  <div>
                    <button class="btn p-0">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="1.6em"
                        height="1.6em"
                        fill="currentColor"
                        class="bi bi-bookmark"
                        viewBox="0 0 16 16"
                      >
                        <path
                          d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"
                        />
                      </svg>
                    </button>
                  </div>
                </div>
                <!-- feed-body-menubar end -->

                <!-- feed-content start -->
                <div class="ps-3 pe-3 pb-2">
                  <strong class="d-block">123 likes</strong>
                  <strong>coco</strong>
                  <span>
                    Lorem ipsum dolor sit amet consectetur adipisicing elit.
                    Accusantium minus, tempore eaque dolorem officiis velit aut
                    quaerat alias, voluptate rerum eos error aliquid. Nobis
                    omnis optio qui accusantium. Nobis, doloribus.
                  </span>
                  <button class="btn p-0 d-block">
                    <span class="text-muted">
                      View all varialble comments
                    </span>
                  </button>
                  <!-- feed-comments-views start -->
                  <div>
                    <div class="mb-1">
                      <strong class="me-2">user_name</strong>
                      <span>comment</span>
                    </div>
                    <div class="mb-1">
                      <strong class="me-2">heex.x</strong>
                      <span>😧😧ㅋㅋㅋㅋ</span>
                    </div>
                  </div>
                  <small class="text-muted">varialble HOUR AGO</small>
                </div>
                <!-- feed-comments-views end -->

                <!-- feed-comment-input start -->
                <div class="position-relative comment-box">
                  <form>
                    <input
                      class="w-100 border-0 p-3"
                      placeholder="Add a comment...."
                    />
                    <button class="btn btn-primary position-absolute btn-ig">
                      Post
                    </button>
                  </form>
                </div>
                <!-- feed-comment-input end -->
              </div>
              <!-- feed-content end -->
            </div>
          </div>
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
export default {
  name: "FeedView",
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
