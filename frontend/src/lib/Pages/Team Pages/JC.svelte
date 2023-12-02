<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import MalakAbdallah from "../../../assets/AC/JC/Malak Abdalla - JC chair.jpg"
    import DalilaMobarak from "../../../assets/AC/JC/Dalila Mobarak - JC co chair.jpg" 
    import KhadijaDarrag from "../../../assets/AC/JC/Khadija Darrag - Junior Committee Co chair.jpg"
    import GroupSection from "../../Components/GroupSection.svelte";
  </script>
  
      <NavBar />
        <header class="px-10">
            <h1 class=" text-4xl font-bold text-center mt-10"> Junior Committee </h1>
            <hr class="mb-2 mt-4">  
        </header>
        <section class="p-10 space-y-6">
            <GroupSection link={null} noReadMe={true} header="Malak Abdallah - Chair of JC" text={null} image={MalakAbdallah} />
            <section class="grid grid-flow-col grid-cols-2 space-x-3">
                <HeadShot name="Dalila Mobarak" title="Co-Chair" image={DalilaMobarak} quote="With determination anything is achievable"/>
                <HeadShot name="Khadija Darrag" title="Co-Chair" image={KhadijaDarrag} quote="Sometimes all you need is a little imagination"/>
            </section>
        </section>
  
      