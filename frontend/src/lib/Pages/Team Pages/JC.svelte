<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import MalakAbdallah from "../../../assets/AC/JC/Malak Abdalla - JC chair.jpg"
    import DalilaMobarak from "../../../assets/AC/JC/Dalila Mobarak - JC co chair.jpg" 
    import KhadijaDarrag from "../../../assets/AC/JC/Khadija Darrag - Junior Committee Co chair.jpg"
  </script>
  
  <body class="bg-cover bg-no-repeat bg-center" >
      <NavBar />
  
      <div class="p-10">
          <h1 class="text-center text-4xl font-bold mb-2"> Junior Committee Chairs</h1>
          <hr class="mb-4">
          <div class="grid grid-flow-row grid-rows-3 space-y-2">
              <section class="grid grid-cols-1 md:grid-cols-2 gap-4 row-span-2 rounded shadow-md">
                  <div class="relative flex p-5">
                      <img src={MalakAbdallah} alt="Person" class="object-cover rounded-lg w-full"/>
                  </div>
                  <div class="flex flex-col justify-between">
                      <div class="">
                          <div class="font-bold text-2xl text-gray-800 mb-3 mt-7">
                              <header>Malak Abdallah - Chair of the Junior Committee</header>
                              <hr>
                          </div>
                          <div>
                              <article class=" text-sm md:text-base">
                                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate 
                              </article>
                          </div>
                      </div> 
                  </div>
              </section>
              <div class="grid grid-cols-2 grid-flow-col space-x-2 ">
                  <HeadShot name="Dalila Mobarak" title="Co-Chair" image={DalilaMobarak} quote="With determination anything is achievable"/>
                  <HeadShot name="Khadija Darrag" title="Co-Chair" image={KhadijaDarrag} quote="Sometimes all you need is a little imaginations"/>
              </div>
          </div>
      </div>
  </body>