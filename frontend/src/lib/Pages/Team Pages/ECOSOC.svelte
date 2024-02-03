<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import OmarEzzi from "../../../assets/AC/ECOSOC-A/OmarElezzi.jpg"
    import SalmaShayal from "../../../assets/AC/ECOSOC-A/SalmaShayal.jpg"
    import AdamYoussef from "../../../assets/AC/ECOSOC-A/AdamYoussef.jpg"
    import AlaaHashem from "../../../assets/AC/ECOSOC-B/AlaaHashem.jpg"
    import HabibaRaslan from "../../../assets/AC/ECOSOC-B/HabibaRaslan.jpg"
    import MahmoudHelmy from "../../../assets/AC/ECOSOC-B/MahmoudHelmy.jpg"
    import GroupSection from "../../Components/GroupSection.svelte";
</script>
  

    <NavBar />

    <header class="px-10">
        <h1 class=" text-4xl font-bold text-center mt-10"> Economic & Social Council A </h1>
        <hr class="mb-2 mt-4">  
    </header>
    <section class="p-10 space-y-6">
        <GroupSection link={null} noReadMe={true} header="Omar Ezzi - Chair of ECOSOC A" text="Hello delegates, I’m Omar, the chair of ECOSOC A. ECOSOC is my favorite committee as I studied similar subjects in school so I can add and utilise my information to guide the subject of the council. I'm very excited to meet you guys and have an enthusiastic debate." image={OmarEzzi} />
        <section class="space-x-0 space-y-2 md:grid md:grid-flow-col md:grid-cols-2 md:space-x-3 md:space-y-0">
            <HeadShot name="Salma Shayal" title="Co-Chair" image={SalmaShayal} quote="Hello! My name is Salma El Shayal. I'm co-chairing ECOSOC. Model United Nations is something I've been interested in since I was twelve. It's something that's really driven me to push my boundaries, step out of my comfort zone and do better."/>
            <HeadShot name="Adam Youssef" title="Co-Chair" image={AdamYoussef} quote="Hello. My name is Adam Youssef,I am the co-chair of Ecosoc. So happy to be a part of ALSMUN 2024 and so happy to see how far it has come ever since it started last year. MUN has become a big part of my life for the past 3 years. It teaches you valuable life skills that are very useful and it's a chance for everyone to have fun while gaining knowledge."/>
        </section>
    </section>
    
    <header class="px-10">
        <h1 class=" text-4xl font-bold text-center mt-6"> Economic & Social Council B </h1>
        <hr class="mb-2 mt-4">  
    </header>
    <section class="p-10 space-y-6">
        <GroupSection link={null} noReadMe={true} header="Alaa Hashem - Chair of ECOSOC B" text="Hello everyone, I’m Alaa and will be chair of ECOSOC B. This is my second time chairing, my first was ALSMUN I where I was co-chair of SC. I think you will all find ECOSOC very entertaining because it covers a wide range of interesting topics. Although my MUN journey ends here, I hope many of you begin yours." image={AlaaHashem} />
        <section class="space-x-0 space-y-2 md:grid md:grid-flow-col md:grid-cols-2 md:space-x-3 md:space-y-0">
            <HeadShot name="Habiba Raslan" title="Co-Chair" image={HabibaRaslan} quote="Welcome to ALSMUNII! We can't wait to see you!"/>
            <HeadShot name="Mahmoud Helmy" title="Co-Chair" image={MahmoudHelmy} quote="Hi Delegates, I am so excited to be you ECOSOC Co-Chair, It's a great honor to be able to chair at ALSMUN. I look forward to meeting all of you."/>
        </section>
    </section>
