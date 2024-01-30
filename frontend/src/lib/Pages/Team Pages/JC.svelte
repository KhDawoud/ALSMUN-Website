<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import MalakAbdallah from "../../../assets/AC/JC/Malak Abdalla - JC chair.jpg"
    import DalilaMobarak from "../../../assets/AC/JC/Dalila Mobarak - JC co chair.jpg" 
    import KhadijaDarrag from "../../../assets/AC/JC/Khadija Darrag - Junior Committee Co chair.jpg"
    import GroupSection from "../../Components/GroupSection.svelte";
    import YousefKhater from"../../../assets/AC/JC/Yousef Khater.jpg";
    import AdamSalem from"../../../assets/AC/JC/Adam Salem.jpg";
    import PlaceHolder from "../../../assets/Icons/Default_pfp.svg"
  </script>
  
      <NavBar />
        <header class="px-10">
            <h1 class=" text-4xl font-bold text-center mt-10"> Junior Committee A </h1>
            <hr class="mb-2 mt-4">  
        </header>
        <section class="p-10 space-y-6">
            <GroupSection link={null} noReadMe={true} header="Malak Abdallah - Chair of JC A" text={"Hey delegates, I'm Malak Abdalla, your chair of Junior Committee A this year. Although I've only been participating in MUN for about a year, I've become very passionate about it and it's now one of my favourite extracurriculars. I'm very excited for my first time chairing junior committee and look forward to a great conference with you guys"} image={MalakAbdallah} />
            <section class="space-x-0 space-y-2 md:grid md:grid-flow-col md:grid-cols-2 md:space-x-3 md:space-y-0">
                <HeadShot name="Dalila Mobarak" title="Co-Chair" image={DalilaMobarak} quote="Hi! I'm Dalila Mobarak and it's my first time co-chairing so I'm super excited. I'm going to study international relations next year at university, partly because of how much I loved all my MUN experiences!"/>
                <HeadShot name="Khadija Darrag" title="Co-Chair" image={KhadijaDarrag} quote="Hey everyone! My name's Khadija Darrag and I'm this year's Co-Chair for junior committee A. I enjoy MUN immensely and can't wait to meet you all and make this MUN the most memorable one."/>
            </section>
        </section>

        <header class="px-10">
            <h1 class=" text-4xl font-bold text-center mt-10"> Junior Committee B </h1>
            <hr class="mb-2 mt-4">  
        </header>
        <section class="p-10 space-y-6">
            <GroupSection link={null} noReadMe={true} header="Yousef Khater - Chair of JC B" text={"Hello, my name is Yousef Khater and I'm the chair for Junior Committee B. Being involved in MUN's has truly made me a more confident and well spoken individual, and I'm really excited to attend the conference and meet the next generation of bright delegates. I hope that during the ALSMUN, I will be able to, as a chair for the first time, alongside my co chairs, provide these young delegates with a great start to their MUN journeys."} image={YousefKhater} />
            <section class="space-x-0 space-y-2 md:grid md:grid-flow-col md:grid-cols-2 md:space-x-3 md:space-y-0">
                <HeadShot name="Adam Salem" title="Co-Chair" image={AdamSalem} quote="Hi all! My name is Adam Salem and I'll be this year's co-chair for junior committee B. I'm sure this committee will be one of the best in all of ALSMUN and I'm really looking forward to meeting everyone and making this MUN memorable!"/>
                <HeadShot name="Joud Khaled" title="Co-Chair" image={PlaceHolder} quote="Hey everyone! My name is Joud Abdelmaguid and I am Co-chairing for junior committee B this year. I am really looking forward to exceeding my knowledge and skills through this ALSMUN experience and hope to encourage all delegates to continue pursuing their MUN journey."/>
            </section>
        </section>
  
      