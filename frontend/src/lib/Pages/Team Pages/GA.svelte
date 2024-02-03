<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import GroupSection from "../../Components/GroupSection.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import KarimElguindy from "../../../assets/AC/GA-A/KarimElguindy.jpg"
    import LaylaMourad from "../../../assets/AC/GA-A/LaylaMourad.jpg"
    import MalakShawky from "../../../assets/AC/GA-B/MalakShawky.jpg"
    import CynthiaEzzi from "../../../assets/AC/GA-B/CynthiaEzzi.jpg"
    import OmarFazary from "../../../assets/AC/GA-B/OmarFazary.jpg"
    import YoussefSherif from "../../../assets/AC/GA-A/YoussefSherif.jpg"
</script>
  

    <NavBar />
    
    <header class="px-10">
        <h1 class=" text-4xl font-bold text-center mt-10"> General Assembly A </h1>
        <hr class="mb-2 mt-4">  
    </header>
    <section class="p-10 space-y-6">
        <GroupSection link={null} noReadMe={true} header="Karim ElGuindy - Chair of GA A" text="Hello everybody, my name is Karim Guindy I will be the chair of GA A this mun. I’m very excited to be chairing for the first open ALSMUN that will be happening this year. I hope this mun will be great." image={KarimElguindy} />
        <section class="space-x-0 space-y-2 md:grid md:grid-flow-col md:grid-cols-2 md:space-x-3 md:space-y-0">
            <HeadShot name="Layla Mourad" title="Co-Chair" image={LaylaMourad} quote="Welcome to ALSMUNII! We can't wait to see you!"/>
            <HeadShot name="Youssef Sheriff" title="Co-Chair" image={YoussefSherif} quote="Hello everyone my name is Youssef and I'm honoured to help in charing GA A as it is a great committee for topics that are too broad for other committees but still just as crucial to our world."/>
        </section>
    </section>
    
    <header class="px-10">
        <h1 class=" text-4xl font-bold text-center mt-6"> General Assembly B </h1>
        <hr class="mb-2 mt-4">  
    </header>
    <section class="p-10 space-y-6">
        <GroupSection link={null} noReadMe={true} header="Omar Fazary - Chair of GA B" text="Hello everyone, my name is Omar Elfazary. I'm in grade 12, and I'm honored to be chairing GA B once more. I have a strong passion for MUN, so I'm looking to seeing some fruitful - and heated - debates this year." image={OmarFazary} />
        <section class="space-x-0 space-y-2 md:grid md:grid-flow-col md:grid-cols-2 md:space-x-3 md:space-y-0">
            <HeadShot name="Malak Shawky" title="Co-Chair" image={MalakShawky} quote="Welcome to ALSMUNII! We can't wait to see you!"/>
            <HeadShot name="Cynthia Ezzi" title="Co-Chair" image={CynthiaEzzi} quote="Hi everyone! My name is Cynthia Ezzi. I'm in grade 10 and so pleased to be co - chairing for the first time in General Assembly B. I'm so excited to meet you all at the conference!"/>
        </section>
    </section>