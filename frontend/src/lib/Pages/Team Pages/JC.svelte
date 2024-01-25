<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import MalakAbdallah from "../../../assets/AC/JC/Malak Abdalla - JC chair.jpg"
    import DalilaMobarak from "../../../assets/AC/JC/Dalila Mobarak - JC co chair.jpg" 
    import KhadijaDarrag from "../../../assets/AC/JC/Khadija Darrag - Junior Committee Co chair.jpg"
    import GroupSection from "../../Components/GroupSection.svelte";
    import YousefKhater from"../../../assets/AC/JC/Yousef Khater.jpg";
    import AdamSalem from"../../../assets/AC/JC/Adam Salem.jpg";
  </script>
  
      <NavBar />
        <header class="px-10">
            <h1 class=" text-4xl font-bold text-center mt-10"> Junior Committee A </h1>
            <hr class="mb-2 mt-4">  
        </header>
        <section class="p-10 space-y-6">
            <GroupSection link={null} noReadMe={true} header="Malak Abdallah - Chair of JC A" text={null} image={MalakAbdallah} />
            <section class="space-x-0 space-y-2 md:grid md:grid-flow-col md:grid-cols-2 md:space-x-3 md:space-y-0">
                <HeadShot name="Dalila Mobarak" title="Co-Chair" image={DalilaMobarak} quote="With determination anything is achievable"/>
                <HeadShot name="Khadija Darrag" title="Co-Chair" image={KhadijaDarrag} quote="Sometimes all you need is a little imagination"/>
            </section>
        </section>

        <header class="px-10">
            <h1 class=" text-4xl font-bold text-center mt-10"> Junior Committee B </h1>
            <hr class="mb-2 mt-4">  
        </header>
        <section class="p-10 space-y-6">
            <GroupSection link={null} noReadMe={true} header="Yousef Khater - Chair of JC B" text={null} image={YousefKhater} />
            <section class="space-x-0 space-y-2 md:grid md:grid-flow-col md:grid-cols-2 md:space-x-3 md:space-y-0">
                <HeadShot name="Adam Salem" title="Co-Chair" image={AdamSalem} quote="With determination anything is achievable"/>
                <HeadShot name="Joud Khaled" title="Co-Chair" image={YousefKhater} quote="Sometimes all you need is a little imagination"/>
            </section>
        </section>
  
      